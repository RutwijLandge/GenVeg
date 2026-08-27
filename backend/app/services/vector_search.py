from pymongo import MongoClient

from app.config import settings
from app.services.embedding_service import generate_embedding


VECTOR_INDEX_NAME = "vector_index"
VECTOR_FIELD = "embedding"


def semantic_search(
    query: str,
    limit: int = 5,
) -> list[dict]:
    client = MongoClient(settings.mongodb_uri)

    db = client[settings.database_name]
    collection = db["products"]

    query_embedding = generate_embedding(query)

    pipeline = [
        {
            "$vectorSearch": {
                "index": VECTOR_INDEX_NAME,
                "path": VECTOR_FIELD,
                "queryVector": query_embedding,
                "numCandidates": 50,
                "limit": limit,
            }
        },
        {
            "$project": {
                "_id": 0,
                "name": 1,
                "category": 1,
                "subcategory": 1,
                "price": 1,
                "unit": 1,
                "description": 1,
                "tags": 1,
                "common_uses": 1,
                "cuisine_types": 1,
                "dietary_info": 1,
                "score": {
                    "$meta": "vectorSearchScore"
                },
            }
        },
    ]

    results = list(collection.aggregate(pipeline))

    client.close()

    return results