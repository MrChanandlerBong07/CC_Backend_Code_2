import sqlite3
import requests
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH = "db/shop_database.db"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"

OAUTH_URL = (
    f"https://accounts.google.com/o/oauth2/v2/auth"
    f"?client_id={CLIENT_ID}"
    f"&response_type=code"
    f"&scope=openid%20email%20profile"
    f"&redirect_uri={REDIRECT_URI}"
)

def sign_up(username: str, password: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT * FROM users WHERE username=?", (username,))
    if cr.fetchone():
        cn.close()
        raise HTTPException(status_code=400, detail="Username exists")
    cr.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
               (username, password, "user"))
    cn.commit()
    cn.close()
    return {"message": "User signed up"}

def users_login(username: str, password: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT * FROM users WHERE username=? AND password=? AND role='user'",
               (username, password))
    if cr.fetchone():
        cn.close()
        return {"message": f"Welcome {username}", "role": "user"}
    cn.close()
    raise HTTPException(status_code=401, detail="Invalid user credentials")

def admin_login(username: str, password: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT * FROM users WHERE username=? AND password=? AND role='admin'",
               (username, password))
    if cr.fetchone():
        cn.close()
        return {"message": f"Welcome {username}", "role": "admin"}
    cn.close()
    raise HTTPException(status_code=401, detail="Invalid admin credentials")

def google_login():
    return {"url": OAUTH_URL}

def google_calling_back(code: str):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    r = requests.post(token_url, data=data)
    if r.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed token")
    tokens = r.json()
    id_info = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={tokens['id_token']}").json()
    return {"message": "Google login successful", "email": id_info.get("email")}
