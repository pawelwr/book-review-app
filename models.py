from application import db
from database import conn



class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.reviews_id = []


class Book:
    def __init__(self, title, author, year, isbn, review_count=0, avarage_score=0.0):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.review_count = review_count
        self.avarage_score = avarage_score

    @classmethod
    def search_by_isbn(self, isbn):
        query = f"SELECT * FROM book WHERE isbn ILIKE '%{isbn}%'"
        cursor = conn.cursor()
        cursor.execute(query)
        book = cursor.fetchall()
        print(book)
        cursor.close()


class Review:
    def __init__(self, book_id, user_id, published, content):
        self.book_id = book_id
        self.user_id = user_id
        self.published = published
        self.content = content