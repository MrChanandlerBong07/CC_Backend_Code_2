from fastapi import APIRouter
from handlers import orders_handlers
from schemas import Place_Order

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/place")
def placing_order(order: Place_Order):
    return orders_handlers.place_order(
        order.user_id, order.address, order.payment_method
    )

@router.get("/history/{user_id}")
def orders_history(user_id: int):
    return orders_handlers.order_history(user_id)
