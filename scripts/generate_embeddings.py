import sys
from pathlib import Path

from pymongo import MongoClient

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.config import settings
from app.services.embedding_service import (
    create_product_text,
    generate_embedding,
)


def generate_product_embeddings():
    client = MongoClient(settings.mongodb_uri)

    db = client[settings.database_name]
    collection = db["products"]

    products = list(collection.find({}))

    print(f"Found {len(products)} products.")

    for product in products:
        product_text = create_product_text(product)
        embedding = generate_embedding(product_text)

        collection.update_one(
            {"_id": product["_id"]},
            {
                "$set": {
                    "embedding": embedding,
                    "embedding_model": "all-MiniLM-L6-v2",
                }
            },
        )

        print(f"Embedded: {product['name']}")

    client.close()

    print("Embedding generation completed.")


if __name__ == "__main__":
    generate_product_embeddings()