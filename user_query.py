
from embedder_sentence_transformer import embed_user_query
from vectorstore import search_pinecone
from llm_gemini_2_5_flash import query_llm_with_context

def process_user_query(query: str):

    # Embed the user's query to create a vector representation
    query_embedding = embed_user_query(query)
    print("Query embedding shape:", len(query_embedding))
    #print("Query embedding:", query_embedding)

    #Search for relevant chunks in Pinecone vector database
    relevant_chunks = search_pinecone(query_embedding, top_k=4, namespace="")
    print("Relevant chunks len:", len(relevant_chunks))

    #Generate answer using retrieved chunks and the user query
    answer = query_llm_with_context(query, relevant_chunks)
    
    return answer

if __name__ == "__main__":
    user_query = "What is the company's policy on remote work?"
    response = process_user_query(user_query)
    print("Answer:", response)