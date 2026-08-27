from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embedding(text: str) -> list[float]:
    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()


def create_product_text(product: dict) -> str:
    return f"""
Product: {product.get("name", "")}
Category: {product.get("category", "")}
Subcategory: {product.get("subcategory", "")}
Description: {product.get("description", "")}
Tags: {", ".join(product.get("tags", []))}
Common uses: {", ".join(product.get("common_uses", []))}
Cuisine: {", ".join(product.get("cuisine_types", []))}
Dietary information: {", ".join(product.get("dietary_info", []))}
Storage: {product.get("storage", "")}
""".strip()