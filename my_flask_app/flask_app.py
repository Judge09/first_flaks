from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)  # Returns the JSON list directly

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8172, debug=True)
