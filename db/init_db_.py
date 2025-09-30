import sqlite3
import os
import time

DB_PATH = "db/shop_database.db"  

def init_db():
    if not os.path.exists("db"):
        os.makedirs("db")
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()

    cr.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    cr.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        description TEXT,
        quantity INTEGER,
        price REAL,
        created REAL,
        restocked REAL
    )
    """)
    cr.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        items TEXT,
        time REAL
    )
    """)

    cn.commit()
    cn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully")
