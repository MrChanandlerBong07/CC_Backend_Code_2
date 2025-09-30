import sqlite3
from fastapi import HTTPException

DB_PATH = "db/shop_database.db"

def past_orders(username: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT * FROM orders WHERE username=?", (username,))
    orders = cr.fetchall()
    cn.close()
    return [{"id": o[0], "username": o[1], "items": o[2]} for o in orders]

def view_orders(username: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT role FROM users WHERE username=?", (username,))
    row = cr.fetchone()
    if not row or row[0] != "admin":
        cn.close()
        raise HTTPException(status_code=403, detail="Admins only")
    cr.execute("SELECT * FROM orders")
    orders = cr.fetchall()
    cn.close()
    return [{"id": o[0], "username": o[1], "items": o[2]} for o in orders]

def revenue(username: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT role FROM users WHERE username=?", (username,))
    row = cr.fetchone()
    if not row or row[0] != "admin":
        cn.close()
        raise HTTPException(status_code=403, detail="Admins only")
    cr.execute("SELECT items FROM orders")
    all_items = cr.fetchall()
    total = 0
    for i in all_items:
        for itm in eval(i[0]):
            total += itm["qty"] * itm["price"]
    cn.close()
    return {"revenue": total}
