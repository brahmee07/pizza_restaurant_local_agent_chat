🧠 Local RAG with LangChain, Ollama, and Chroma

This is a simple Retrieval-Augmented Generation (RAG) application, built as part of my self-learning journey. It demonstrates how to integrate LangChain, Ollama, and ChromaDB to create a question-answering system based on restaurant reviews. Everything runs locally — there's no need for API keys or cloud services, making it entirely offline and private.

I built this project by teaching myself through online resources like YouTube tutorials, Google searches, and ChatGPT conversations. I explored documentation, experimented with code, and iterated through various implementations to better understand how these technologies work together. This hands-on approach helped solidify my knowledge of RAG systems and local LLM pipelines.

🛠️ Technologies Used

LangChain – for building the RAG pipeline and managing the flow between components

Ollama – for running large language models like llama3 locally, without any cloud dependencies

ChromaDB – a local vector database to store and retrieve embedded document chunks

Pandas – to load and process the dataset (realistic_restaurant_reviews.csv)

Python – the entire application is written in Python

Terminal / CLI – the interface is simple and runs in the command line


🍕 What This Project Does

Loads a dataset of restaurant reviews (focused on pizza places) from a CSV file.

Splits and embeds the reviews using a local embedding model (mxbai-embed-large via Ollama).

Stores the embedded data in ChromaDB for fast vector search.

Allows the user to ask natural language questions like:

"What are the best pizzas in town?"

"Do any places have vegan options?"

"What do people say about the crust?"

Retrieves the most relevant reviews from the dataset using vector similarity search.

Feeds those reviews, along with your question, into a local LLM (llama3.2) to generate an answer — all without using the internet or sending data to external servers.

🚀 How to Run This Project Locally

Install Ollama
Make sure you have Ollama installed and running. You can install it using:
curl -fsSL https://ollama.com/install.sh | sh

Then start the Ollama service:
ollama serve


And pull the models you'll need:
ollama pull llama3
ollama pull mxbai-embed-large

Create a Virtual Environment 
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Required Python Packages
pip install -r requirements.txt

Run the Script
python app.py


Once it starts, you can type your questions in the terminal, like:

What are the best pizza places?

Which restaurants have gluten-free or vegan options?

What do customers say about delivery service?

Type q to quit.


🔧 Troubleshooting

If you encounter issues with Ollama or the Llama model, ensure that the correct version of Ollama is installed and that the model is running.

If the chroma_langchain_db/ folder isn’t being created, double-check your Chroma and LangChain setup.

🧑‍💻 Contributing

This project is a self-learning initiative. However, contributions are welcome! If you have suggestions for improving the code or any questions about the setup, feel free to create an issue or submit a pull request.

