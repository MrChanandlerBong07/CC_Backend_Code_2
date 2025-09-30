from pydantic import BaseModel, EmailStr
from typing import Optional

class User_Signup(BaseModel):
    username: str
    password: str

class User_Login(BaseModel):
    username: str
    password: str

class Add_Inventory_Item(BaseModel):
    name: str
    type: str
    refillable: bool
    quantity: int
    price: float

class Add_To_Cart(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class Place_Order(BaseModel):
    user_id: int
    address: str
    payment_method: str
