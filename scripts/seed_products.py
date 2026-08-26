import sys
from pathlib import Path

from pymongo import MongoClient, UpdateOne

# Allow the script to import the backend app package.
BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.config import settings


PRODUCTS = [
    # Root vegetables
    {
        "name": "Potato",
        "category": "Vegetable",
        "subcategory": "Root Vegetable",
        "price": 35,
        "unit": "kg",
        "description": "Fresh potatoes suitable for curries, fries, snacks and everyday cooking.",
        "tags": ["cooking", "curry", "fries", "snacks", "indian"],
        "common_uses": ["aloo sabzi", "fries", "paratha", "samosa"],
        "cuisine_types": ["Indian", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Store in a cool, dark and dry place.",
    },
    {
        "name": "Carrot",
        "category": "Vegetable",
        "subcategory": "Root Vegetable",
        "price": 60,
        "unit": "kg",
        "description": "Fresh crunchy carrots suitable for salads, soups, juices and cooking.",
        "tags": ["healthy", "salad", "soup", "juice"],
        "common_uses": ["salad", "soup", "juice", "gajar halwa"],
        "cuisine_types": ["Indian", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate in a vegetable drawer.",
    },
    {
        "name": "Beetroot",
        "category": "Vegetable",
        "subcategory": "Root Vegetable",
        "price": 55,
        "unit": "kg",
        "description": "Fresh beetroot suitable for salads, juices and healthy meals.",
        "tags": ["healthy", "salad", "juice"],
        "common_uses": ["salad", "juice", "roasted vegetables"],
        "cuisine_types": ["Indian", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and keep dry.",
    },
    {
        "name": "Radish",
        "category": "Vegetable",
        "subcategory": "Root Vegetable",
        "price": 40,
        "unit": "kg",
        "description": "Fresh crunchy radish suitable for salads, parathas and Indian meals.",
        "tags": ["salad", "healthy", "paratha", "indian"],
        "common_uses": ["salad", "mooli paratha", "pickle"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate after removing the leaves.",
    },

    # Fruit vegetables
    {
        "name": "Tomato",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 40,
        "unit": "kg",
        "description": "Fresh red tomatoes suitable for curries, salads, sauces and soups.",
        "tags": ["cooking", "salad", "indian", "curry", "sauce"],
        "common_uses": ["curry", "salad", "sauce", "soup"],
        "cuisine_types": ["Indian", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Store at room temperature and refrigerate when fully ripe.",
    },
    {
        "name": "Capsicum",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 80,
        "unit": "kg",
        "description": "Fresh green capsicum suitable for pizza, noodles, stir-fries and curries.",
        "tags": ["pizza", "noodles", "stir-fry", "curry"],
        "common_uses": ["pizza", "noodles", "fried rice", "curry"],
        "cuisine_types": ["Indian", "Chinese", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate in a breathable bag.",
    },
    {
        "name": "Green Chilli",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 70,
        "unit": "kg",
        "description": "Fresh green chillies used to add heat and flavor to Indian dishes.",
        "tags": ["spicy", "indian", "curry", "seasoning"],
        "common_uses": ["curry", "chutney", "tadka", "pickle"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate in a sealed container.",
    },
    {
        "name": "Brinjal",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 50,
        "unit": "kg",
        "description": "Fresh brinjal suitable for curries, roasting and Indian vegetable dishes.",
        "tags": ["curry", "roasting", "indian"],
        "common_uses": ["baingan bharta", "bharit", "curry"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and consume within a few days.",
    },

    # Leafy vegetables
    {
        "name": "Spinach",
        "category": "Vegetable",
        "subcategory": "Leafy Vegetable",
        "price": 30,
        "unit": "bunch",
        "description": "Fresh green spinach suitable for soups, curries, salads and healthy meals.",
        "tags": ["healthy", "leafy", "soup", "curry"],
        "common_uses": ["palak paneer", "soup", "salad", "smoothie"],
        "cuisine_types": ["Indian", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and consume within 3-4 days.",
    },
    {
        "name": "Coriander",
        "category": "Herb",
        "subcategory": "Leafy Herb",
        "price": 20,
        "unit": "bunch",
        "description": "Fresh coriander leaves used for garnishing curries, chutneys and meals.",
        "tags": ["garnish", "indian", "curry", "herb"],
        "common_uses": ["garnish", "chutney", "curry"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate wrapped in a damp paper towel.",
    },
    {
        "name": "Mint",
        "category": "Herb",
        "subcategory": "Leafy Herb",
        "price": 25,
        "unit": "bunch",
        "description": "Fresh mint leaves suitable for chutneys, drinks, salads and Indian dishes.",
        "tags": ["herb", "chutney", "drink", "indian"],
        "common_uses": ["mint chutney", "pudina rice", "raita", "drinks"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate in a damp paper towel.",
    },

    # Cruciferous vegetables
    {
        "name": "Cauliflower",
        "category": "Vegetable",
        "subcategory": "Cruciferous",
        "price": 50,
        "unit": "piece",
        "description": "Fresh cauliflower suitable for curries, stir-fries, roasting and snacks.",
        "tags": ["curry", "stir-fry", "snacks", "indian"],
        "common_uses": ["gobi manchurian", "aloo gobi", "pakora", "roast"],
        "cuisine_types": ["Indian", "Chinese"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate in a perforated bag.",
    },
    {
        "name": "Cabbage",
        "category": "Vegetable",
        "subcategory": "Cruciferous",
        "price": 45,
        "unit": "kg",
        "description": "Fresh cabbage suitable for salads, stir-fries, noodles and Indian cooking.",
        "tags": ["salad", "stir-fry", "noodles", "indian"],
        "common_uses": ["coleslaw", "stir-fry", "noodles", "sabzi"],
        "cuisine_types": ["Indian", "Chinese", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and keep dry.",
    },
    {
        "name": "Broccoli",
        "category": "Vegetable",
        "subcategory": "Cruciferous",
        "price": 100,
        "unit": "kg",
        "description": "Fresh broccoli suitable for roasting, soups, salads and stir-fries.",
        "tags": ["healthy", "salad", "soup", "roast"],
        "common_uses": ["soup", "stir-fry", "roasted vegetables", "salad"],
        "cuisine_types": ["Continental", "Chinese"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and consume within a few days.",
    },

    # Other vegetables
    {
        "name": "Cucumber",
        "category": "Vegetable",
        "subcategory": "Fruit Vegetable",
        "price": 45,
        "unit": "kg",
        "description": "Fresh cucumbers suitable for salads, raita and refreshing meals.",
        "tags": ["salad", "healthy", "refreshing", "raita"],
        "common_uses": ["salad", "raita", "sandwich", "detox water"],
        "cuisine_types": ["Indian", "Continental"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and keep dry.",
    },
    {
        "name": "Green Peas",
        "category": "Vegetable",
        "subcategory": "Legume",
        "price": 90,
        "unit": "kg",
        "description": "Fresh green peas suitable for curries, pulao, rice dishes and snacks.",
        "tags": ["curry", "pulao", "rice", "snacks", "indian"],
        "common_uses": ["matar paneer", "pulao", "fried rice", "samosa"],
        "cuisine_types": ["Indian", "Chinese"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and use within a few days.",
    },
    {
        "name": "Bottle Gourd",
        "category": "Vegetable",
        "subcategory": "Gourd",
        "price": 40,
        "unit": "kg",
        "description": "Fresh bottle gourd suitable for curries, soups and traditional Indian dishes.",
        "tags": ["healthy", "curry", "soup", "indian"],
        "common_uses": ["lauki sabzi", "lauki soup", "kofta"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate and consume within several days.",
    },
    {
        "name": "Bitter Gourd",
        "category": "Vegetable",
        "subcategory": "Gourd",
        "price": 70,
        "unit": "kg",
        "description": "Fresh bitter gourd commonly used in Indian curries and stir-fries.",
        "tags": ["healthy", "curry", "indian", "stir-fry"],
        "common_uses": ["karela sabzi", "stuffed karela", "stir-fry"],
        "cuisine_types": ["Indian"],
        "dietary_info": ["vegetarian", "vegan"],
        "storage": "Refrigerate in a breathable bag.",
    },
]


def seed_database():
    client = MongoClient(settings.mongodb_uri)
    db = client[settings.database_name]
    collection = db["products"]

    operations = []

    for product in PRODUCTS:
        operations.append(
            UpdateOne(
                {"name": product["name"]},
                {
                    "$set": product,
                    "$setOnInsert": {
                        "freshness": "Fresh",
                        "organic": False,
                    },
                },
                upsert=True,
            )
        )

    if operations:
        result = collection.bulk_write(operations)

        print(f"Matched: {result.matched_count}")
        print(f"Modified: {result.modified_count}")
        print(f"Inserted: {len(result.upserted_ids)}")

    print(f"Seed catalog contains {collection.count_documents({})} products.")

    client.close()


if __name__ == "__main__":
    seed_database()