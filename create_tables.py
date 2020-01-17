from application import db
from database import conn

cursor = conn.cursor()

cursor.execute("""CREATE TABLE users (
    id serial PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL,
    email VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL
    );
    
CREATE TABLE book (
    id serial PRIMARY KEY,
    title VARCHAR,
    author VARCHAR,
    year INTEGER NOT NULL,
    isbn VARCHAR UNIQUE NOT NULL
    );
    
CREATE TABLE review (
    id serial PRIMARY KEY,
    book_id INTEGER REFERENCES book(id),
    user_id INTEGER REFERENCES users(id),
    published TIMESTAMP,
    content VARCHAR (500) NOT NULL
    );
    """)

conn.commit()
cursor.close()
conn.close()