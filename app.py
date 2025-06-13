from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Author, Book, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Get all books with authors and reviews
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

# Get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id, description="Book not found")
    return jsonify(book.to_dict()), 200

# Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'year', 'author_id')):
        abort(400, description="Missing title, year, or author_id")
    
    # Check if author exists
    author = Author.query.get(data['author_id'])
    if not author:
        abort(400, description="Author not found")

    try:
        book = Book(title=data['title'], year=data['year'], author_id=data['author_id'])
        db.session.add(book)
        db.session.commit()
        return jsonify(book.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Update a book's title or year
@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    book = Book.query.get_or_404(id, description="Book not found")
    data = request.get_json()
    if not data:
        abort(400, description="No data provided")

    book.title = data.get('title', book.title)
    book.year = data.get('year', book.year)
    db.session.commit()
    return jsonify(book.to_dict()), 200

# Delete a book and its reviews
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id, description="Book not found")
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': f'Book {book.title} and its reviews were deleted.'}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
