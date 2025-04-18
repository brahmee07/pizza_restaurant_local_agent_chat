from langchain_ollama.llms import OllamaLLM # Import the language model from langchain_ollama
from langchain_core.prompts import ChatPromptTemplate  # Import the chat prompt template class to create structured prompts
from vector import retriever # Import the retriever object from vector.py (used to search the review database)


# Initialize the language model with the specified model name ("llama3.2")
model = OllamaLLM(model="llama3.2")

# Define the template that tells the model how to respond
# This gives the model some relevant reviews and the user's question
template = """
You are an expert in answering questions about a pizza restaurant

Here some relevant reviews: {reviews}

Here is the question to answer: {question}

"""

prompt = ChatPromptTemplate.from_template(template) # Create a ChatPromptTemplate from the string template above
chain = prompt | model   #Take the output from prompt, and pass it directly into model.

while True:
    print("----------------------------------------")
    question = input("Ask your question(q to quit)")
    if question == "q":
        break
    print("----------------------------------------")
    
    # Use the retriever to get the top relevant reviews based on the question
    reviews = retriever.invoke(question)
    
    # Use the model to generate a response based on the reviews and the user's question
    result = chain.invoke({"reviews": reviews, "question":question})
    print(result)
