import csv

from application import db
from database import conn

cursor = conn.cursor()


def main():   
    f = open("books.csv")   
    reader = csv.reader(f, delimiter=",")    
    for isbn, title, author, year in reader:
        if isbn=="isbn": continue
        if "'" in title:
            t = title.split("'")
            title = "''".join(t)
        if "'" in author:
            t = author.split("'")
            author = "''".join(t)
        query = f"INSERT INTO book (isbn, title, author, year) VALUES ('{isbn}', '{title}', '{author}', {year})"
        print(query)
        cursor.execute(query)
    conn.commit()

main()

cursor.close()
conn.close()