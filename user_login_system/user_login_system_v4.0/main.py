from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Ethan's Portal Login API V4.0")

user_database = {"User": "123456"} 
ADMIN_PASSWORD = "admin123" # 保留原来的管理员密码

# 定义前端传数据的格式
class AuthData(BaseModel):
    username: str
    password: str

class ResetData(BaseModel):
    confirm: str
    admin_password: str

# ================= API 接口区 =================

# 1. Sign UP
@app.post("/signup")
def signup(data: AuthData):
    name = data.username
    pswd = data.password
    
    if name in user_database:
        raise HTTPException(status_code=400, detail="❌ FAILURE: The user ALREADY EXISTS!")
    elif len(pswd) != 6:
        raise HTTPException(status_code=400, detail="❌ FAILURE: It must be a 6-DIGIT PASSWORD!")
    else:
        user_database[name] = pswd
        return {"message": "✅ ACCESS!"}

# 2. Sign IN
@app.post("/signin")
def signin(data: AuthData):
    user = data.username
    pwd = data.password
    
    if user in user_database and user_database[user] == pwd:
        return {"message": "✅ ACCESS!"}
    else:
        raise HTTPException(status_code=401, detail="❌ FAILURE: INCORRECT username or password!")

# 3. Log OFF
@app.post("/logoff")
def logout(data: AuthData):
    user = data.username
    pwd = data.password
    
    if user in user_database and user_database[user] == pwd:
        del user_database[user]
        return {"message": "✅ Account LOG OFF!"}
    else:
        raise HTTPException(status_code=401, detail="❌ FAILURE: INCORRECT username or password!")

# ================= ADMINISTRATOR =================
# 1. VIEW all users
@app.get("/admin/users")
def get_users(admin_password: str):
    if admin_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="❌ ACCESS DENIED!")
    return {"Current User Database": user_database}

# 2. ADD user
@app.post("/admin/add_user")
def admin_add_user(admin_password: str, data: AuthData):
    if admin_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="❌ ACCESS DENIED!")
        
    name = data.username
    pswd = data.password
    
    if name in user_database:
        raise HTTPException(status_code=400, detail="❌ FAILURE: The user ALREADY EXISTS!")
    elif len(pswd) != 6:
        raise HTTPException(status_code=400, detail="❌ FAILURE: It must be a 6-DIGIT PASSWORD!")
    else:
        user_database[name] = pswd
        return {"message": "✅ User ADDED!"}

# 3. REMOVE user
@app.delete("/admin/remove_user")
def admin_remove_user(admin_password: str, username: str):
    if admin_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="❌ ACCESS DENIED!")
        
    if username in user_database:
        del user_database[username]
        return {"message": "✅ User REMOVED!"}
    else:
        raise HTTPException(status_code=404, detail="❌ FAILURE: The user does NOT EXIST!")

# 4. RESET system
@app.post("/admin/reset")
def admin_reset(data: ResetData):
    if data.admin_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="❌ ACCESS DENIED!")
        
    if data.confirm.lower() == "yes":
        user_database.clear()
        return {"message": "✅ System RESET! All users have been deleted."}
    else:
        raise HTTPException(status_code=400, detail="❌ System RESET CANCELLED.")