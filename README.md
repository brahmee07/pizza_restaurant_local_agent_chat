# pizza_restaurant_local_agent_chat

# 🧠 Local RAG with LangChain, Ollama, and Chroma

This is a simple, local Retrieval-Augmented Generation (RAG) application built entirely as a self-learning project. I explored the world of LangChain, Ollama, and ChromaDB to understand how to implement question-answering over a set of documents — specifically, restaurant reviews.

## 🛠️ What I Did

- I started with a dataset of realistic restaurant reviews in CSV format.
- Then I used `Ollama` locally to run an LLM (I chose `llama3.2`) without needing any API keys or cloud-based services.
- Using `LangChain`, I connected everything together — from the embedding model to the retriever to the final prompt and output.
- I stored and queried the vectorized documents using `Chroma`, a lightweight, local vector database.
- All of this runs locally on my Mac — offline!

This was purely a self-driven learning journey, mostly pieced together from online tutorials, LangChain documentation, and lots of trial-and-error.

## 📁 Project Structure

```bash
.
├── main.py                # Runs the RAG pipeline interactively
├── vector.py              # Handles vector database creation and retrieval logic
├── realistic_restaurant_reviews.csv  # Dataset used for retrieval
├── requirements.txt       # Python dependencies
├── README.md              # You're reading it
├── chroma_langchain_db/   # Auto-generated DB folder after first run
└── A_flowchart...png      # A visual overview of the system
