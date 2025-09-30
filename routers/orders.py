from fastapi import APIRouter
from handlers import orders_handlers

router = APIRouter()

@router.get("/past")
def past_orders(username: str):
    return orders_handlers.past_orders(username)

@router.get("/inventory/orders")
def view_orders(username: str):
    return orders_handlers.view_orders(username)

@router.get("/inventory/revenue")
def revenue(username: str):
    return orders_handlers.revenue(username)
