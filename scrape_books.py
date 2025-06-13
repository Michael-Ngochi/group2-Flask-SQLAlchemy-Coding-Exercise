import requests
from bs4 import BeautifulSoup
from app import app, db
from models import Author, Book

def scrape_and_store_books():
    with app.app_context():
        # Using Project Gutenberg as a sample source
        url = "https://www.gutenberg.org/ebooks/search/?sort_order=downloads"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            books_added = 0
            authors_added = 0
            
            # Find book listings (adjust selectors based on actual site structure)
            book_elements = soup.select('.booklink')[:5]  # Limit to 5 books
            
            for book_elem in book_elements:
                title_elem = book_elem.select_one('.title')
                author_elem = book_elem.select_one('.subtitle')
                
                if not title_elem or not author_elem:
                    continue
                    
                title = title_elem.text.strip()
                author_name = author_elem.text.strip()
                
                # Check if author exists, create if not
                author = Author.query.filter_by(name=author_name).first()
                if not author:
                    author = Author(name=author_name)
                    db.session.add(author)
                    db.session.commit()
                    authors_added += 1
                
                # Add book (using a default year since Gutenberg may not provide it)
                book = Book(
                    title=title,
                    publication_year=1800,  # Default year for demo
                    author_id=author.id
                )
                db.session.add(book)
                books_added += 1
            
            db.session.commit()
            return {
                'books_added': books_added,
                'authors_added': authors_added,
                'message': 'Scraping completed successfully'
            }
            
        except requests.RequestException as e:
            return {
                'error': f'Failed to scrape data: {str(e)}'
            }

if __name__ == '__main__':
    print(scrape_and_store_books())