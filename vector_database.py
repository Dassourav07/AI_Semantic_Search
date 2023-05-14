import pinecone
from vectorization_algorithm import encode_text
import pinecone_index

class VectorDatabase:
    def __init__(self):
        # Initialize Pinecone vector database
        pinecone.init(api_key="75f10981-72d9-46f7-83be-7e8d0290f80a")
        self.index = pinecone.Index(index_name="my_index")

    def add_document(self, document_id, text):
        # Encode text document into vector representation
        document_vector = encode_text(text)

        # Add vector representation to vector database
        pinecone_index.upsert(ids=document_id, vectors=document_vector)

    def get_vector(self, document_id):
        # Retrieve vector representation from vector database
        return pinecone_index.retrieve(ids=document_id)

