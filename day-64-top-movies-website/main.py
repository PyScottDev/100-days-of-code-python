from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv
import os

load_dotenv()
MOVIE_API = os.getenv("MOVIE_API_KEY")
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
SELECT_URL = "https://api.themoviedb.org/3/movie"


BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
db_path = os.path.join(BASE_DIR, "top-movies.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = db.mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = db.mapped_column(db.String(250), unique=True, nullable=False)
    year: Mapped[int] = db.mapped_column(db.Integer, nullable=False)
    description: Mapped[str] = db.mapped_column(db.String(500), nullable=False)
    rating: Mapped[float] = db.mapped_column(db.Float, nullable=True)
    ranking: Mapped[int] = db.mapped_column(db.Integer, nullable=True)
    review: Mapped[str] = db.mapped_column(db.String(250), nullable=True)
    img_url: Mapped[str] = db.mapped_column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

    
# CREATE TABLE
class EditMovie(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Edit Movie")
    
class AddMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(
        db.select(Movie).order_by(Movie.rating.desc())
    )   
    all_movies = result.scalars().all()
    for i, movie in enumerate(all_movies, start=1):
        movie.ranking = i

    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditMovie()
    if form.validate_on_submit():
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        found_movies = search_movie(form.title.data)
        return render_template("select.html", movies=found_movies)
    return render_template("add.html", form=form)

def search_movie(movie_search):
    params = {
    "api_key": MOVIE_API,
    "query": movie_search,
    }
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    result = response.json()
    found_movies = result["results"]
    return found_movies    

@app.route("/select/<int:movie_id>")
def select(movie_id):
    params = {"api_key": MOVIE_API}

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    result = response.json()

    release_date = result.get("release_date")
    poster_path = result.get("poster_path")

    movie_add = Movie(
        title=result.get("title"),
        description=result.get("overview"),
        year=int(release_date[:4]) if release_date else None,
        img_url=f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None,
    )

    db.session.add(movie_add)
    db.session.commit()
    return redirect(url_for("edit", movie_id=movie_add.id))

    
    

if __name__ == '__main__':
    app.run(debug=True)
