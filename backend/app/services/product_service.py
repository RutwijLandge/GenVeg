from typing import Any

from bson import ObjectId

from app.database import db


products_collection = db["products"]


def create_product(product_data: dict[str, Any]) -> str:
    result = products_collection.insert_one(product_data)
    return str(result.inserted_id)


def get_all_products() -> list[dict[str, Any]]:
    products = list(products_collection.find())

    for product in products:
        product["id"] = str(product["_id"])
        del product["_id"]

    return products


def get_product_by_id(product_id: str) -> dict[str, Any] | None:
    if not ObjectId.is_valid(product_id):
        return None

    product = products_collection.find_one(
        {"_id": ObjectId(product_id)}
    )

    if product is None:
        return None

    product["id"] = str(product["_id"])
    del product["_id"]

    return product


def search_products(query: str) -> list[dict[str, Any]]:
    products = list(
        products_collection.find(
            {
                "$or": [
                    {"name": {"$regex": query, "$options": "i"}},
                    {"category": {"$regex": query, "$options": "i"}},
                    {"description": {"$regex": query, "$options": "i"}},
                    {"tags": {"$regex": query, "$options": "i"}},
                ]
            }
        )
    )

    for product in products:
        product["id"] = str(product["_id"])
        del product["_id"]

    return products