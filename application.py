import os
import psycopg2
import requests

from flask import Flask, session, render_template, request, redirect, flash, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from datetime import datetime

from database import conn, gr_key
from models import Book, User, Review
from forms import LoginForm

app = Flask(__name__)
DATABASE_URL = "postgres://dyqjdqmwzfzjvw:1183c33c8bb8e2eb63c31da1f6496db492462e67c02d67ceec95a0e3caf25821@ec2-54-75-238-138.eu-west-1.compute.amazonaws.com:5432/dehg1it917u19a"


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "ppp"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

login_manager = LoginManager()
login_manager.init_app(app)



@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/", methods=["POST"])
def search():
    text = request.form.get("search")
    print(text)
    result = Book.search(text)
    print(result)
    return render_template("search_result.html", text=text, result=result)

@login_manager.user_loader
def load_user(username):
    query = f"SELECT username, password, email, id FROM users WHERE username = '{username}' OR email = '{username}'"
    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    cursor.close()
    if user:
        username = user[0]
        password = user[1]
        email = user [2]
        id = user[3]
        return User(id, username, password, email)
    return None

@app.route("/book/<int:id>")
def book_page(id):
    book = Book.search_by_id(id)
    try:
        gr_data = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": f"{gr_key}", "isbns": f"{id}"})
        gr_json = gr_data.json()
        avg_rank = gr_json['books'][0]['average_rating']
        num_ratings = gr_json['books'][0]['work_ratings_count']
    except:
        avg_rank = 'no data'
        num_ratings = 'no data'
    
    comments = Book.get_comments(id)
    return render_template("book_page.html", avg_rank=avg_rank, num_ratings=num_ratings, book=book, comments=comments)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = load_user(username)
        password = form.password.data

        print(user)

        if user and password == user.password:
            login_user(user)

        if user is None or not current_user.is_authenticated:
            flash('Invalid username or password')
            print("nouser")
            return redirect("/login")

        return render_template("layout.html")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@login_required
@app.route("/comment/<int:book_id>", methods=['POST'])
def add_comment(book_id):
    text = request.form.get("add_comment")
    print(text)
    published = datetime.now()
    user_id = current_user.id
    Review.add_coment(book_id, user_id, published, text)
    return redirect(f"/book/{book_id}")
