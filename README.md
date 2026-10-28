# 🥦 GenVeg — GenAI Grocery Shopping Assistant

GenVeg is a conversational grocery shopping assistant designed to help users discover relevant vegetables and grocery products using natural-language queries. It uses semantic search to retrieve products based on the meaning of a query rather than relying only on exact keyword matches.

## 🚀 Features

- **Product Management APIs:** Create, retrieve, and search products using FastAPI.
- **MongoDB Integration:** Store and manage product information in MongoDB Atlas.
- **Semantic Search:** Retrieve relevant products using natural-language queries.
- **Text Embeddings:** Generate 384-dimensional embeddings using `all-MiniLM-L6-v2`.
- **Vector Search:** Use MongoDB Atlas Vector Search with cosine similarity.
- **Embedding Pipeline:** Generate and store embeddings for product records.
- **Product Catalog:** Maintain structured information such as names, categories, prices, descriptions, tags, common uses, and dietary information.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API development |
| MongoDB Atlas | Product database |
| Sentence Transformers | Embedding generation |
| `all-MiniLM-L6-v2` | Embedding model |
| MongoDB Atlas Vector Search | Semantic retrieval |
| Uvicorn | API server |

## 🧠 How It Works

1. Product information is stored in MongoDB Atlas.
2. The embedding model converts product information into 384-dimensional vectors.
3. The vectors are stored in MongoDB alongside product records.
4. A user submits a natural-language search query.
5. The query is converted into an embedding using the same model.
6. MongoDB Atlas Vector Search retrieves relevant products using cosine similarity.
7. The retrieved products provide the foundation for a Retrieval-Augmented Generation (RAG) pipeline.

**Example query:**  
`I want healthy vegetables for dinner`

The semantic search system can retrieve relevant products such as carrots, spinach, broccoli, capsicum, and tomatoes.

## 🏗️ Project Structure

```text
genveg-ai/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── schemas/
│   │   ├── services/
│   │   │   ├── product_service.py
│   │   │   ├── embedding_service.py
│   │   │   └── vector_search.py
│   │   └── routes/
│   │       └── products.py
│   ├── requirements.txt
│   └── .env
├── scripts/
│   ├── seed_products.py
│   ├── generate_embeddings.py
│   ├── test_embedding.py
│   └── test_vector_search.py
├── frontend/
├── docs/
└── .gitignore
```

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/RutwijLandge/GenVeg.git
cd GenVeg
```

### 2. Create and activate a virtual environment

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `backend` directory:

```env
MONGODB_URI=your_mongodb_atlas_connection_string
DATABASE_NAME=genveg
```

Use the exact environment variable names expected by your `config.py`. Never commit database credentials or API tokens.

### 5. Seed product data and generate embeddings

From the project root, with the virtual environment activated:

```powershell
python scripts/seed_products.py
python scripts/generate_embeddings.py
```

Ensure MongoDB Atlas has a Vector Search index named `vector_index` on the `embedding` field, configured for 384 dimensions and cosine similarity.

### 6. Start the API server

From the `backend` directory:

```powershell
uvicorn app.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## 🔍 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/api/products/` | Create a product |
| GET | `/api/products/` | Retrieve products |
| GET | `/api/products/search?q=tomato` | Search products |
| GET | `/api/products/semantic-search?q=healthy%20vegetables` | Semantic product search |
| GET | `/api/products/{product_id}` | Retrieve a product by ID |

## 🎯 Project Objectives

- Improve product discovery using semantic search.
- Build a modular backend for a conversational shopping application.
- Establish the retrieval component of a RAG architecture.
- Explore embeddings and vector databases for GenAI applications.

## 🔮 Future Improvements

- Integrate an instruction-tuned LLM for natural-language responses grounded in retrieved products.
- Implement LLM tool calling for product search, inventory validation, and price lookup.
- Develop a conversational frontend.
- Add retrieval evaluation, automated tests, and response-quality monitoring.

## 👨‍💻 Author

**Rutwij Landge**

- GitHub: [RutwijLandge](https://github.com/RutwijLandge)

---

*GenVeg is a work in progress. The current implementation focuses on backend APIs, product data management, embedding generation, and semantic retrieval. LLM-based response generation and agentic tool calling are planned enhancements.*
