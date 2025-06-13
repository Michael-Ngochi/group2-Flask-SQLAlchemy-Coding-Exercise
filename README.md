**Book Review**

*Features*

- Create, retrieve, update, and delete books
- Manage authors
- view reviews for books
- Flask-SQLAlchemy ORM with relationships
- Database migrations using Flask-Migrate

Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (for local development)
- Requests & BeautifulSoup4 (for optional web scraping)

Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Michael-Ngochi/group2-Flask-SQLAlchemy-Coding-Exercise.git
cd group2-Flask-SQLAlchemy-Coding-Exercise
```
2. Create a virtual environment & activate it:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize and migrate the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Seed the database:
```bash
python seed.py
```
6. Run the application:
```bash
flask run
```
API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /books | Get all books |
| GET | /books/`id` | Get book by ID |
| POST | /books | Create a new book |
| PATCH | /books/`id` | Update book details |
| DELETE | /books/`id` | Delete a book and its reviews |


