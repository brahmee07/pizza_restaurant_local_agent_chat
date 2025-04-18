from langchain_ollama import OllamaEmbeddings # For generating embeddings using an Ollama-supported model
from langchain_community.vectorstores import Chroma  # Chroma is the vector database used to store/retrieve embeddings
from langchain_core.documents import Document # Document class for creating structured data to store in Chroma
import os # To check if files or directories exist
import pandas as pd 


df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model = "mxbai-embed-large") # Initialize the embedding model using Ollama

db_location = "./chroma_langchain_db" # Define the folder where the vector database will be stored


# Check if the folder exists — if not, we need to add the documents to the database
add_documents = not os.path.exists(db_location) 

# If it's a new database, prepare the documents to add
if add_documents:
    documents = [] #to store document objects
    ids = [] #to store unique string ids for each documents
    
    
    # Loop through each row in the CSV and create Document objects
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"], # Combine title and review as the main content
            metadata={"rating":row["Rating"], "date":row["Date"]},  # Add extra info as metadata
            id = str(i) # Unique ID for the document (required by Chroma)
            
        )
        ids.append(str(i))
        documents.append(document)
        

# Initialize the Chroma vector store        
vector_store = Chroma(
    collection_name = "restaurant_reviews",
    persist_directory = db_location,
    embedding_function = embeddings,
)


# If we created new documents earlier, now we add them to the Chroma database
if add_documents:
    vector_store.add_documents(documents = documents, ids = ids)
    
    
# Create a retriever from the vector store to fetch the top 5 most relevant documents
retriever = vector_store.as_retriever(
    search_kwargs = {"k": 5}  # k = 5 means it returns the 5 most similar reviews for a given query 
)
        

