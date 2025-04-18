🧠 Local RAG with LangChain, Ollama, and Chroma

This is a simple Retrieval-Augmented Generation (RAG) application designed as a self-learning project. It explores the integration of LangChain, Ollama, and ChromaDB to implement a question-answering system using restaurant reviews as the dataset. The entire setup is local, meaning you don’t need API keys or cloud-based services — everything runs offline on your machine!

This project was driven by my self-learning journey. I leveraged online resources, including YouTube, Google, and ChatGPT, to piece together the concepts and tools required to implement this solution. Through experimentation and iterating on different approaches, I used tutorials and documentation from various platforms to gain hands-on experience and improve my understanding of these technologies.

🚀 What It Does

This project allows you to:

Use a dataset of restaurant reviews to answer questions.

Leverage LangChain for orchestration between the embedding model, retriever, and LLM.

Run an Ollama LLM (llama3.2) locally without API keys.

Store and query vectorized documents using Chroma, a local vector database.

The goal of this project was to understand how to implement Retrieval-Augmented Generation (RAG) with local models and databases while experimenting with the various components.


🛠️ What I Used
LangChain: Used for connecting the various components of the RAG pipeline, including the embedding model and document retrieval.

Ollama (Llama 3.2): Local LLM that performs the question-answering without the need for external API keys.

Chroma: A lightweight local vector database that stores and retrieves vectorized representations of the restaurant review documents.


Python: The core programming language used for implementing the pipeline.

📁 Project Structure

├── main.py                        # Entry point to run the RAG pipeline interactively

├── vector.py                      # Handles vector database creation and retrieval logic

├── realistic_restaurant_reviews.csv  # Dataset used for retrieval

├── requirements.txt               # List of Python dependencies

├── chroma_langchain_db/           # Folder generated by Chroma to store the database


main.py: This file runs the entire RAG pipeline. It takes input from the user (a question), uses LangChain for orchestration, fetches relevant documents using Chroma, and generates an answer using the locally running Llama model.

vector.py: Contains the logic for vectorizing the restaurant reviews and interacting with the Chroma vector database.

realistic_restaurant_reviews.csv: A dataset of restaurant reviews in CSV format used for the RAG system.

requirements.txt: Lists the necessary Python libraries to run the project.

chroma_langchain_db/: Folder automatically created after the first run, storing the Chroma vector database.

📥 Installation & Setup

Follow these steps to run this project locally:

 Clone the Repository
git clone https://github.com/brahmee07/pizza_restaurant_local_agent_chat.git
cd pizza_restaurant_local_agent_chat

 Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install the Required Python Packages
pip install -r requirements.txt

Install Ollama (if not already installed)
You will need Ollama to run the Llama 3.2 model locally. Follow the installation instructions from the Ollama website.

After installing Ollama, ensure it is running locally. You can check if the model is available by running:
ollama run llama3.2

Run the Application

Once all dependencies are installed, you can run the interactive application by executing main.py:
python main.py

You will be prompted to enter a question related to the restaurant reviews, and the system will provide a relevant answer based on the dataset.

📝 Usage

Ask Questions

When you run main.py, it will prompt you to input a question (e.g., "What are the most common complaints about this restaurant?"). The system will search through the restaurant reviews dataset, retrieve relevant documents, and provide an answer using the Llama 3.2 model.

Chroma Database

After the first run, Chroma will create a database in the chroma_langchain_db/ folder to store the vectorized documents. This allows for faster document retrieval during subsequent runs.

View Results

The application will output the generated response based on the relevant restaurant reviews retrieved from the Chroma database.

🔧 Troubleshooting

If you encounter issues with Ollama or the Llama model, ensure that the correct version of Ollama is installed and that the model is running.

If the chroma_langchain_db/ folder isn’t being created, double-check your Chroma and LangChain setup.

🧑‍💻 Contributing

This project is a self-learning initiative. However, contributions are welcome! If you have suggestions for improving the code or any questions about the setup, feel free to create an issue or submit a pull request.

