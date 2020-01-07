from application import db

db.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY
    email VARCHAR NOT NULL
    password VARCHAR NOT NULL
    )""")