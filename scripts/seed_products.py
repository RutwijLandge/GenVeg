import sys
from pathlib import Path

# Add the backend directory to Python's import path
BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.config import settings
from pymongo import MongoClient


products = [
    {
        "name": "Tomato",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 40,
        "unit": "kg",
        "stock": 100,
        "description": "Fresh red tomatoes suitable for curries, salads and sauces.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["cooking", "salad", "indian", "curry"],
    },
    {
        "name": "Potato",
        "category": "Vegetable",
        "subcategory": "Root Vegetable",
        "price": 35,
        "unit": "kg",
        "stock": 150,
        "description": "Fresh potatoes suitable for frying, curries and snacks.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["cooking", "frying", "curry", "snacks"],
    },
    {
        "name": "Onion",
        "category": "Vegetable",
        "subcategory": "Bulb Vegetable",
        "price": 45,
        "unit": "kg",
        "stock": 120,
        "description": "Fresh onions suitable for curries, salads and cooking.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["cooking", "salad", "curry", "indian"],
    },
    {
        "name": "Carrot",
        "category": "Vegetable",
        "subcategory": "Root Vegetable",
        "price": 60,
        "unit": "kg",
        "stock": 80,
        "description": "Fresh crunchy carrots suitable for salads, soups and cooking.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["healthy", "salad", "soup", "snacks"],
    },
    {
        "name": "Capsicum",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 80,
        "unit": "kg",
        "stock": 70,
        "description": "Fresh green capsicum suitable for pizza, noodles and curries.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["pizza", "noodles", "curry", "indian"],
    },
    {
        "name": "Cauliflower",
        "category": "Vegetable",
        "subcategory": "Cruciferous",
        "price": 50,
        "unit": "piece",
        "stock": 60,
        "description": "Fresh cauliflower suitable for curries, stir fry and snacks.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["curry", "stir-fry", "snacks", "indian"],
    },
    {
        "name": "Spinach",
        "category": "Vegetable",
        "subcategory": "Leafy Vegetable",
        "price": 30,
        "unit": "bunch",
        "stock": 90,
        "description": "Fresh green spinach suitable for soups, curries and healthy meals.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["healthy", "leafy", "soup", "curry"],
    },
    {
        "name": "Cucumber",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 45,
        "unit": "kg",
        "stock": 85,
        "description": "Fresh cucumbers suitable for salads and refreshing meals.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["salad", "healthy", "refreshing"],
    },
    {
        "name": "Green Peas",
        "category": "Vegetable",
        "subcategory": "Legume",
        "price": 90,
        "unit": "kg",
        "stock": 50,
        "description": "Fresh green peas suitable for curries, pulao and snacks.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["curry", "pulao", "snacks", "indian"],
    },
    {
        "name": "Coriander",
        "category": "Herb",
        "subcategory": "Leafy Herb",
        "price": 20,
        "unit": "bunch",
        "stock": 100,
        "description": "Fresh coriander leaves used for garnishing curries and meals.",
        "freshness": "Fresh",
        "organic": False,
        "tags": ["garnish", "indian", "curry", "herb"],
    },
]


def seed_database():
    client = MongoClient(settings.mongodb_uri)
    db = client[settings.database_name]
    collection = db["products"]

    collection.delete_many({})

    result = collection.insert_many(products)

    print(f"Inserted {len(result.inserted_ids)} products.")

    client.close()


if __name__ == "__main__":
    seed_database()