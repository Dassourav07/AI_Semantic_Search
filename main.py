from flask import Flask, render_template, request
from vector_database import VectorDatabase
from vectorization_algorithm import encode_text
from similarity_search_algorithm import find_similar_documents

app = Flask(__name__)

# Initialize vector database
db = VectorDatabase()

# Define routes
@app.route("/")
def home():
    return render_template("Home.html")



@app.route("/search", methods=["POST"])
def search():
    # Get user query
    query = request.form["query"]

    # Encode user query
    query_vector = encode_text(query)

    # Find similar documents
    similar_documents = find_similar_documents(query_vector, db)

    # Render search results template with similar documents
    return render_template("Results.html", query=query, similar_documents=similar_documents)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True, use_reloader=True)
    