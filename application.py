import os
import psycopg2

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
DATABASE_URL = "postgres://dyqjdqmwzfzjvw:1183c33c8bb8e2eb63c31da1f6496db492462e67c02d67ceec95a0e3caf25821@ec2-54-75-238-138.eu-west-1.compute.amazonaws.com:5432/dehg1it917u19a"

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():

    return "Project 1: TODO"
