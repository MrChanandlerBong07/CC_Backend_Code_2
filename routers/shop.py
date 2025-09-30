from fastapi import APIRouter
from handlers import shop_handlers

router = APIRouter(prefix="/shop", tags=["shop"])

@router.get("/list")
def shop():
    return shop_handlers.shop_list()
