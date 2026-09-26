from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api", tags=["Required endpoints"])

# Demo-only in-memory data; resets when the process restarts.
CATALOG = [
    {"id": 1, "name": "Compute", "price": 100},
    {"id": 2, "name": "Storage", "price": 50},
    {"id": 3, "name": "Database", "price": 75},
]

class OrderRequest(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class ItemUpdate(BaseModel):
    name: str = Field(min_length=1)

@router.get("/GetCatalog")
def GetCatalog():
    return {"items": CATALOG}

@router.post("/CreateOrder", status_code=201)
def CreateOrder(order: OrderRequest):
    product = next((p for p in CATALOG if p["id"] == order.product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Order created", "order": {
        "product_id": product["id"], "product_name": product["name"],
        "quantity": order.quantity, "total": product["price"] * order.quantity,
    }}

@router.put("/UpdateItem/{item_id}")
def UpdateItem(item_id: int, update: ItemUpdate):
    item = next((p for p in CATALOG if p["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item["name"] = update.name
    return {"message": "Item updated", "item": item}
