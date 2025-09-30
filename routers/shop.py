from fastapi import APIRouter
from handlers import shop_handlers

router = APIRouter()

@router.get("/list")
def shop_list():
    return shop_handlers.shop_list()
