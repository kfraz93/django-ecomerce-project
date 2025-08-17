from datetime import datetime

from ninja import Schema

class AddToCartSchema(Schema):
    item_id: int

class RemoveFromCartSchema(Schema):
    item_id: int

class ItemSchema(Schema):
    id: int
    name: str
    price: float
    description: str

class CartItemSchema(Schema):
    id: int
    item: ItemSchema
    created: datetime
