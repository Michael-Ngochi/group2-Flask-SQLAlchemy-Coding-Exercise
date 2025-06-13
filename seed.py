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
        book1 = Book(title="Pride and Prejudice", publication_year=1813, author_id=author1.id)
        book2 = Book(title="Sense and Sensibility", publication_year=1811, author_id=author1.id)
        book3 = Book(title="1984", publication_year=1949, author_id=author2.id)
        book4 = Book(title="Animal Farm", publication_year=1945, author_id=author2.id)
        db.session.add_all([book1, book2, book3, book4])
        db.session.commit()

        # Create reviews
        review1 = Review(rating=5, comment="Amazing romance novel!")
        review2 = Review(rating=4, comment="Great characters")
        review3 = Review(rating=5, comment="Dystopian masterpiece")
        review4 = Review(rating=4, comment="Thought-provoking")
        review5 = Review(rating=3, comment="Good but slow start")
        review6 = Review(rating=5, comment="Really enjoyed this!")

        # Associate reviews with books
        book1.reviews.extend([review1, review2])
        book2.reviews.append(review5)
        book3.reviews.extend([review3, review4])
        book4.reviews.append(review6)
        
        
        db.session.add_all([review1, review2, review3, review4, review5, review6])
        db.session.commit()

if __name__ == '__main__':
    seed_database()