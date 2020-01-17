# from application import db
from database import conn
from application import *


class User():
    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.authenticated = False
        self.reviews_id = []

    @classmethod
    def add_user(self, username, password, email):
        query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')"
        print(query)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return True

    def __repr__(self):
        return f"<username: {self.username}, password: {self.password}, email: {self.email}>"

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Book:
    def __init__(self, title, author, year, isbn, review_count=0, avarage_score=0.0):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.review_count = review_count
        self.avarage_score = avarage_score

    # @classmethod
    # def search_by_isbn(self, isbn):
    #     query = f"SELECT * FROM book WHERE isbn ILIKE '%{isbn}%'"
    #     cursor = conn.cursor()
    #     cursor.execute(query)
    #     book = cursor.fetchall()
    #     cursor.close()

    @classmethod
    def search(self, text):
        # if "'" in text:
        #     t = text.split("'")
        #     text = "''".join(t)
        query = f"SELECT title, author, year, id, isbn FROM book WHERE title ILIKE '%{text}%' OR author ILIKE '%{text}%'"

        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(query)
        print(result)
        cursor.close()        

        return result

    @classmethod
    def search_by_id(self, id):
        query = f"SELECT title, author, year, id FROM book WHERE id = '{id}'"
        cursor = conn.cursor()
        cursor.execute(query)
        book = cursor.fetchone()
        cursor.close()

        return book
    
    @classmethod
    def get_comments(self, id):
        query = f"SELECT content, published from review WHERE book_id = {id}"
        cursor = conn.cursor()
        cursor.execute(query)
        comments = cursor.fetchall()
        cursor.close()        
        return comments


class Review:
    def __init__(self, book_id, user_id, published, content):
        self.book_id = book_id
        self.user_id = user_id
        self.published = published
        self.content = content

    @classmethod
    def add_coment(self, book_id, user_id, published, content):
        query=f"INSERT INTO review (book_id, user_id, published, content) VALUES ({book_id}, {user_id}, '{published}', '{content}')"
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()