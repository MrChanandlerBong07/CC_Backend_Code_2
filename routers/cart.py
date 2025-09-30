from fastapi import APIRouter
from handlers import cart_handlers
from schemas import Add_To_Cart

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/add")
def adding_to_cart(cart_item: Add_To_Cart):
    return cart_handlers.add_to_cart(
        cart_item.user_id, cart_item.product_id, cart_item.quantity
    )

@router.get("/view/{user_id}")
def viewing_cart(user_id: int):
    return cart_handlers.view_cart(user_id)

@router.post("/checkout")
def checking_out(user_id: int):
    return cart_handlers.checkout(user_id)
