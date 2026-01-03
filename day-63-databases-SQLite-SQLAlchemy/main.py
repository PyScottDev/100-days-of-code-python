from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
db_path = os.path.join(BASE_DIR, "books-collection.db")

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = db.mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = db.mapped_column(db.String(250), unique=True, nullable=False)
    author: Mapped[str] = db.mapped_column(db.String(250), nullable=False)
    rating: Mapped[float] = db.mapped_column(db.Float, nullable=False)
    
with app.app_context():
    db.create_all()


#all_books = []


@app.route('/')
def home():
    result = db.session.execute(
        db.select(Book).order_by(Book.title)
    )
    all_books = result.scalars().all()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
            )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html')

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book_to_update = db.get_or_404(Book, book_id)
    if request.method == "POST":
        book_to_update.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book_to_update)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

    
# with app.app_context():
#     new_book = Book(
#         title=request.form["title"],
#         author=request.form["author"],
#         rating=request.form["rating"]
#         )
#     db.session.add(new_book)
#     db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)

