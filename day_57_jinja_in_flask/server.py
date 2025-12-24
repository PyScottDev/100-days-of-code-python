from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    year = datetime.now().year
    number = random.randint(1, 10)
    return render_template("index.html", num=number, year=year)

@app.route("/guess/<name>")
def guess(name):
    parameters = {
        "name": name
    }
    age_guess = requests.get("https://api.agify.io?", params=parameters)
    age_guess.raise_for_status()
    age_data = age_guess.json()
    age = age_data["age"]

    gender_guess = requests.get("https://api.genderize.io?", params=parameters)
    gender_guess.raise_for_status()
    gender_data = gender_guess.json()
    gender = gender_data["gender"]
    name_formatted = name.title()
    return render_template("guess.html", name=name_formatted, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    blog_posts = blog_response.json()
    return render_template("blog.html", blog_posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)