from fastapi import APIRouter
from handlers import inventory_handlers

router = APIRouter()

@router.get("/list")
def list_items(username: str):
    return inventory_handlers.list_items(username)

@router.post("/new")
def add_item(username: str, name: str, category: str, description: str, quantity: int, price: float):
    return inventory_handlers.add_item(username, name, category, description, quantity, price)
