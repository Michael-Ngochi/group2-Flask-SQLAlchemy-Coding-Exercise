from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Author, Book, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)# Initialize the database
migrate = Migrate(app, db)# Initialize Flask-Migrate

# Get all books with their authors
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

# Get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict()), 200

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    try:
        book = Book(title=data['title'], year=data['year'], author_id=data['author_id'])
        db.session.add(book)
        db.session.commit()
        return jsonify(book.to_dict()), 201
    except Exception as e:
        abort(400, str(e))

# Update a book's details
@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.year = data.get('year', book.year)
    db.session.commit()
    return jsonify(book.to_dict()), 200

# Delete a book and its reviews
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    Review.query.filter_by(book_id=id).delete()
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=1==1)  # Set debug to True for development

