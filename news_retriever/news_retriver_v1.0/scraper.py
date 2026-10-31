import requests
from bs4 import BeautifulSoup
import re
import time
import random

def fetch_news(keyword):
    print(f"[*] Fetching latest news for: '{keyword}'...")
    url = f"https://www.baidu.com/s?wd={keyword}&tn=news"
    
    # Defense 1: Dynamic User-Agent rotation (Disguise as different browsers)
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
    ]
    headers = {"User-Agent": random.choice(user_agents)}
    
    try:
        # Defense 2: Random delay (Mimic human behavior to avoid rate limits)
        time.sleep(random.uniform(1.0, 3.0)) 
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for item in soup.find_all('h3'):
            title = item.get_text(strip=True)
            if title and len(title) > 5:
                # Clean text using Regex
                clean_title = re.sub(r'[【】\s]', '', title)
                results.append(clean_title)
                
        return results[:5]
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Network Error: {e}")
        return []
    except Exception as e:
        print(f"[!] Parsing Error: {e}")
        return []

if __name__ == "__main__":
    # Test execution
    news_list = fetch_news("Artificial Intelligence")
    if news_list:
        print("\n[+] Successfully retrieved data:")
        for idx, news in enumerate(news_list, 1):
            print(f"{idx}. {news}")
    else:
        print("[-] Failed to retrieve data.")