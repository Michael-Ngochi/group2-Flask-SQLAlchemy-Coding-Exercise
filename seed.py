from app import app, db
from models import Author, Book, Review

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create authors
        author1 = Author(name="Jane Austen")
        author2 = Author(name="George Orwell")
        db.session.add_all([author1, author2])
        db.session.commit()

        # Create books
        book1 = Book(title="Pride and Prejudice", year=1813, author_id=author1.id)
        book2 = Book(title="Sense and Sensibility", year=1811, author_id=author1.id)
        book3 = Book(title="1984", year=1949, author_id=author2.id)
        book4 = Book(title="Animal Farm", year=1945, author_id=author2.id)
        db.session.add_all([book1, book2, book3, book4])
        db.session.commit()

        # Create reviews with book_id
        review1 = Review(rating=5, comment="Amazing romance novel!", book_id=book1.id)
        review2 = Review(rating=4, comment="Great characters", book_id=book1.id)
        review3 = Review(rating=5, comment="Dystopian masterpiece", book_id=book3.id)
        review4 = Review(rating=4, comment="Thought-provoking", book_id=book3.id)
        review5 = Review(rating=3, comment="Good but slow start", book_id=book2.id)
        review6 = Review(rating=5, comment="Really enjoyed this!", book_id=book4.id)
        
        db.session.add_all([review1, review2, review3, review4, review5, review6])
        db.session.commit()

if __name__ == '__main__':
    seed_database()