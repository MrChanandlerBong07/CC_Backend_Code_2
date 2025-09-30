from fastapi import APIRouter
from handlers import cart_handlers

router = APIRouter()

@router.post("/add")
def add_to_cart(username: str, product_id: int, qty: int):
    return cart_handlers.add_to_cart(username, product_id, qty)

@router.get("/info")
def cart_info(username: str):
    return cart_handlers.cart_info(username)

@router.post("/checkout")
def checkout(username: str):
    return cart_handlers.checkout(username)
