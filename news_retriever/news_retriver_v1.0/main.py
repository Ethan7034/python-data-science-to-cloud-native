from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from scraper import fetch_news
from datetime import datetime, time
import os

app = FastAPI(title="News Retriever API - Secured by Edge Layer")

# --- 1. Passive Anti-Scraping (Rate Limiting) ---
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- 2. Edge Security Layer (Mini-WAF & SLA) ---
@app.middleware("http")
async def edge_security_and_sla_middleware(request: Request, call_next):
    
    # --- A. SLA Service Window (09:30 - 21:30) ---
    current_time = datetime.now().time()
    start_time = time(9, 30)
    end_time = time(21, 30)
    
    if not (start_time <= current_time <= end_time):
        return JSONResponse(
            status_code=503,
            content={"detail": "❌Service is currently closed. Our SLA window is 09:30 - 21:30."}
        )

    # --- B. Mini-WAF (Bot Fight Mode) ---
    user_agent = request.headers.get("user-agent", "").lower()
    
    # Block known scraping libraries and empty User-Agents (basic bot fight)
    malicious_bots = ["python-requests", "scrapy", "curl", "wget", "postman"]
    
    if not user_agent or any(bot in user_agent for bot in malicious_bots):
        return JSONResponse(
            status_code=403, 
            content={"detail": "⚠️Forbidden: Malicious bot traffic detected by WAF."}
        )

    # If passed, proceed to the endpoint
    response = await call_next(request)
    return response

# --- 3. API Endpoints ---
@app.get("/")
def read_root():
    html_path = os.path.join(os.path.dirname(__file__),"index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.get("/api/search")
@limiter.limit("5/minute") # Rate limit: 5 requests per minute per IP
async def search_news(request: Request, keyword: str):
    news_data = fetch_news(keyword)
    if not news_data:
        raise HTTPException(status_code=404, detail="❌No news found or scraping failed.")
    return {
        "status": "success",
        "keyword": keyword,
        "data": news_data
    }