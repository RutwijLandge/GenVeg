import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.services.vector_search import semantic_search


query = "I want healthy vegetables for dinner"

results = semantic_search(query, limit=5)

print("\nSemantic Search Results")
print("=" * 50)

for index, product in enumerate(results, start=1):
    print(f"\n{index}. {product['name']}")
    print(f"   Category: {product.get('category')}")
    print(f"   Price: ₹{product.get('price')} / {product.get('unit')}")
    print(f"   Score: {product.get('score')}")
    print(f"   Description: {product.get('description')}")