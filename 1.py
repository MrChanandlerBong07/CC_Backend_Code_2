import sqlite3
import os

DB_PATH = "db/shop_database.db"

def init_db():
    if not os.path.exists("db"):
        os.makedirs("db")
    cn = sqlite3.connect(DB_PATH)
    cr = cn.cursor()

    # Users table
    cr.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Inventory table
    cr.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        description TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Orders table
    cr.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        items TEXT
    )
    """)

    # Preload inventory
    inventory_data = [
        (1, "Pilot V7", "Ink", "Refillable", 10, 50),
        (2, "Pentel Energel", "Gel-Ink", "Refillable", 5, 60),
        (3, "Pentonic", "Ballpen", "Non-Refillable", 50, 10),
        (4, "Schneider", "Ink", "Refillable", 10, 50)
    ]
    cr.executemany("""
        INSERT OR IGNORE INTO inventory (id, name, category, description, quantity, price)
        VALUES (?, ?, ?, ?, ?, ?)
    """, inventory_data)

    # Preload users
    users_data = [
        ("Spiderman", "webs", "user"),
        ("Ironman", "jarvis", "user"),
        ("Superman", "kryptonite", "user"),
        ("Deadpool", "ryan", "user"),
        ("Wolverine", "claws", "user"),
        ("testuser", "testpass", "user"),
        ("testusername", "1234", "user")
    ]
    cr.executemany("""
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES (?, ?, ?)
    """, users_data)

    cn.commit()
    cn.close()
    print("Database initialized with default inventory and users.")

if __name__ == "__main__":
    init_db()

