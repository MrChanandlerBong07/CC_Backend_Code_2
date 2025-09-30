import sqlite3
from fastapi import HTTPException

DB_PATH = "db/shop_database.db"
carts = {}

def add_to_cart(username: str, product_id: int, qty: int):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT * FROM inventory WHERE id=?", (product_id,))
    item = cr.fetchone()
    if not item:
        cn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    if item[4] < qty:
        cn.close()
        raise HTTPException(status_code=400, detail="Not enough stock")
    if username not in carts:
        carts[username] = []
    carts[username].append({"product_id": product_id, "name": item[1], "qty": qty, "price": item[5]})
    cn.close()
    return {"message": "Added to cart"}

def cart_info(username: str):
    if username not in carts:
        return {"cart": [], "total": 0}
    total = sum(c["qty"] * c["price"] for c in carts[username])
    return {"cart": carts[username], "total": total}

def checkout(username: str):
    if username not in carts or not carts[username]:
        raise HTTPException(status_code=400, detail="Cart empty")
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("INSERT INTO orders (username, items) VALUES (?, ?)", 
               (username, str(carts[username])))
    cn.commit()
    cn.close()
    carts[username] = []
    return {"message": "Order placed"}
