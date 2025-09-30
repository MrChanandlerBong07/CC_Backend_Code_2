from fastapi import APIRouter
from handlers import auth_handlers
from schemas import User_Signup, User_Login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/user/signup")
def sign_up(user: User_Signup):
    return auth_handlers.signup(user.username, user.password)

@router.post("/user/login")
def logging_in(user: User_Login):
    return auth_handlers.user_login(user.username, user.password)

@router.post("/admin/login")
def admin_logging_in(username: str, password: str):
    return auth_handlers.admin_login(username, password)
