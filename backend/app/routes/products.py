from fastapi import APIRouter, HTTPException, Query

from app.schemas.product import ProductCreate
from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    search_products,
)


router = APIRouter(
    prefix="/api/products",
    tags=["Products"],
)


@router.post("/")
def add_product(product: ProductCreate):
    product_id = create_product(product.model_dump())

    return {
        "message": "Product created successfully",
        "id": product_id,
    }


@router.get("/")
def get_products():
    return get_all_products()


@router.get("/search")
def search_product_catalog(
    q: str = Query(..., min_length=1)
):
    return search_products(q)


@router.get("/{product_id}")
def get_product(product_id: str):
    product = get_product_by_id(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product