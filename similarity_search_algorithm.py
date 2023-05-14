import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_documents(query_vector, vector_database):
    # Retrieve all vectors from vector database
    all_vectors = vector_database.get_all_vectors()

    # Compute cosine similarity between query vector and all vectors in database
    similarities = cosine_similarity(query_vector, all_vectors)

    # Sort documents by similarity and return top 10
    similar_documents = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:10]

    return similar_documents