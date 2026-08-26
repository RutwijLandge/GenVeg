from pydantic import BaseModel, Field
from typing import List


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    category: str
    subcategory: str | None = None
    price: float = Field(..., gt=0)
    unit: str
    stock: int = Field(..., ge=0)
    description: str
    freshness: str = "Fresh"
    organic: bool = False
    tags: List[str] = []


class ProductResponse(ProductCreate):
    id: str