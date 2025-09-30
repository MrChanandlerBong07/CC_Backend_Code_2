from fastapi import APIRouter
from handlers import inventory_handlers
from schemas import Add_Inventory_Item

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/list")
def list_of_the_inventory(username: str):
    return inventory_handlers.list_inventory(username)

@router.post("/new")
def adding_to_inventory(item: Add_Inventory_Item, username: str):
    return inventory_handlers.add_inventory(
        username, item.name, item.type, item.refillable, item.quantity, item.price
    )
