from fastapi import APIRouter
from handlers import auth_handlers

router = APIRouter()

@router.post("/user/signup")
def signup(username: str, password: str):
    return auth_handlers.signup(username, password)

@router.post("/user/login")
def user_login(username: str, password: str):
    return auth_handlers.user_login(username, password)

@router.post("/admin/login")
def admin_login(username: str, password: str):
    return auth_handlers.admin_login(username, password)

@router.get("/google")
def google_login():
    return auth_handlers.google_login()

@router.get("/google/callback")
def google_callback(code: str):
    return auth_handlers.google_callback(code)
