from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    books = db.relationship('Book', backref='author', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [book.title for book in self.books]
        }

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    reviews = db.relationship('Review', backref='book', cascade='all, delete-orphan', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'author': self.author.name if self.author else None,
            'reviews': [review.to_dict() for review in self.reviews]
        }

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'comment': self.comment
        }
