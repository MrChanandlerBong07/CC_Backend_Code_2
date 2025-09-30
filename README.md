This is a small shop backend project I built using FastAPI and SQLite.

The backend lets you:

Sign up & login users (normal + Google login)

Add inventory (admin only)

Browse items in the shop

Add to cart & checkout

Place orders and track revenue

Here’s how I split my files:

shop_backend/
│
├── main.py             
│
├── routers/            
│   ├── auth.py
│   ├── inventory.py
│   ├── shop.py
│   ├── cart.py
│   └── orders.py
│
├── handlers/           
│   ├── auth_handlers.py
│   ├── inventory_handlers.py
│   ├── shop_handlers.py
│   ├── cart_handlers.py
│   └── orders_handlers.py
│
├── db/
│   ├── init_db.py      
│   └── shop_database.db 
│
├── .env                
└── requirements.txt     

main.py is the entry point

routers contains endpoints (URLs like /auth/signup)

handlers does the work (database queries, logic)

db has the database and script to set it up

.env  keeps secrets safe


How Code Works:

Think of it like this:

You hit an endpoint → e.g. /auth/user/signup

That goes to a router → which only knows “call the handler”

The handler does the actual job → e.g. insert user into DB

The DB stores everything → users, items, orders

Response comes back → simple JSON message


Install the libraries:

pip install fastapi uvicorn requests python-dotenv


Setup the database (creates tables + adds sample data):

python db/init_db.py


Start the server:

uvicorn main:app --reload


Go to:

http://127.0.0.1:8000



Signup:
POST /auth/user/signup?username=test&password=1234

Login (user):
POST /auth/user/login?username=test&password=1234

Login (admin):
POST /auth/admin/login?username=admin&password=adminpass

List shop items:
GET /shop/list

Add to cart:
POST /cart/add?username=test&product_id=1&qty=2

Checkout:
POST /cart/checkout?username=test

See orders:
GET /orders/past?username=test


The .db file is the database 

.env is just a file to keep private stuff (Google login keys).

You can open the database with DB Browser for SQLite to see tables.
