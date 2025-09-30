from fastapi import FastAPI
from routers import auth, inventory, shop, cart, orders

app = FastAPI(title="Shop Backend")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
app.include_router(shop.router, prefix="/shop", tags=["Shop"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def home():
    return {"Msg": "Shop backend running"}
