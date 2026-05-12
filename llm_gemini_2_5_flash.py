from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configure Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def query_llm_with_context(query: str, context: str):

    print("Query to Gemini:", query)
    
    # 1. Define the System Instruction (Equivalent to OpenAI's system role)
    system_instruction = """
    You are a helpful assistant for answering user queries based on provided context. 
    Use the context to provide accurate and relevant answers. 
    Do not make assumptions beyond the context provided. 
    Let the user know if you cannot provide an answer based on the given context.
    """

    # 2. Generate content with specific configuration
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Recommended model for RAG in 2026
        contents=f"Query: {query}\nContext: {context}",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.4
        )
    )

    #print("Gemini response:", response.text)
    return response.text
