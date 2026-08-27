from app.services.embedding_service import generate_embedding


text = """
Tomato. Fresh red tomatoes suitable for curries, salads,
sauces and soups. Category: Vegetable.
Uses: curry, salad, sauce, soup.
Cuisine: Indian, Continental.
Tags: cooking, salad, indian, curry, sauce.
Diet: vegetarian, vegan.
"""


embedding = generate_embedding(text)

print("Embedding generated successfully!")
print("Embedding dimensions:", len(embedding))
print("First 5 values:", embedding[:5])