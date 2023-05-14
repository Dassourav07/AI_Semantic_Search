import pinecone

def pinecone_index(data, ids):
    # Create Pinecone index
    pinecone_index = pinecone.Index(index_name="text_search")

    # Index data
    pinecone_index.upsert(ids=ids, vectors=data)

    # Return index object
    return pinecone_index