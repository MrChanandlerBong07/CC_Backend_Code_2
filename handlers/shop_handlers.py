import sqlite3

DB_PATH = "db/shop_database.db"

def shop_list():
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()
    cr.execute("SELECT id, name, price, quantity FROM inventory")
    items = cr.fetchall()
    cn.close()
    return [{"id": i[0], "name": i[1], "price": i[2], "quantity": i[3]} for i in items]
