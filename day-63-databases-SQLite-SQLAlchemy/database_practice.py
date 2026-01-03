import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
#db_path = os.path.join(BASE_DIR, "new-books-collection.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR}/new-books-collection.db"

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()
    
with app.app_context():
    new_book = Book(
        title="Harry Potter",
        author="J. K. Rowling",
        rating=9.3
    )
    db.session.add(new_book)
    db.session.commit()



# db = sqlite3.connect("day-63-databases-SQLite-SQLAlchemy/books-collection.db")
# cursor = db.cursor()

# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# #cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")


# cursor.execute(
#     "INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
#     ("Harry Potter", "J. K. Rowling", 9.3)
# )

# db.commit()