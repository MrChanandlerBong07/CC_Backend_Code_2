import sqlite3
from fastapi import HTTPException

DB_PATH = "db/shop_database.db"

def list_of_items(username: str):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT role FROM users WHERE username=?", (username,))
    row = cr.fetchone()
    if not row or row[0] != "admin":
        cn.close()
        raise HTTPException(status_code=403, detail="Admins only")
    cr.execute("SELECT * FROM inventory")
    items = cr.fetchall()
    cn.close()
    return [dict(id=i[0], name=i[1], category=i[2], description=i[3],
                 quantity=i[4], price=i[5]) for i in items]

def adding_item(username: str, name: str, category: str, description: str, quantity: int, price: float):
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT role FROM users WHERE username=?", (username,))
    row = cr.fetchone()
    if not row or row[0] != "admin":
        cn.close()
        raise HTTPException(status_code=403, detail="Admins only")
    cr.execute("""INSERT INTO inventory (name, category, description, quantity, price)
                  VALUES (?, ?, ?, ?, ?)""",
               (name, category, description, quantity, price))
    cn.commit()
    item_id = cr.lastrowid
    cn.close()
    return {"message": "Item added", "id": item_id}
