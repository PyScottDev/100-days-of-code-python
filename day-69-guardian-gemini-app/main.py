from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,URL
import guardian
import gemini
from dotenv import load_dotenv
import os

#topic = "politics"
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)

class TopicForm(FlaskForm):
   topic = SelectField(
    "Topic",
    choices=[
        ("world", "World News"),
        ("technology", "Technology"),
        ("society", "Society & Daily Life"),
        ("environment", "Environment & Climate"),
        ("culture", "Culture (Film, Music, TV)"),
        ("sport", "Sport"),
        ("science", "Science & Health"),
        ("business", "Business & Work"),
    ],
   )
   english_level = SelectField(
       "English Level",
       choices=[
           ("a1", "Elementary"),
           ("a2", "Pre-intermediate"),
           ("b1", "Intermediate"),
           ("b2", "Upper intermediate")
       ]
   )
   
   topic_choice = SubmitField("Choose Topic")

@app.route('/', methods=["GET", "POST"])
def home():
   form = TopicForm()
   if form.validate_on_submit():
      topic = form.topic.data
      english_level = form.english_level.data
      return redirect(url_for('article_headings', topic=topic, level=english_level))
   return render_template("index.html", form=form)

@app.route('/headings/<topic>/<level>')
def article_headings(topic, level):
   all_content = guardian.get_articles(topic)
   simplified_headlines = gemini.simplify_headline(all_content, level)
   for post in all_content:
        s = simplified_headlines.get(post.id)
        if s:
            post.simple_title = s["headline"]
            post.simple_subtitle = s["subheadline"]
        else:
            post.simple_title = post.title
            post.simple_subtitle = post.subtitle
   return render_template("headlines.html", all_posts=all_content, topic=topic, level=level)

@app.route("/post/<path:article_id>/<level>")  
def get_article(article_id, level):
   article_obj = guardian.get_body(article_id)
   simplified_body = gemini.simplify_body(article_obj, level)
   article_obj.simple_title = simplified_body["headline"]
   article_obj.simple_subtitle = simplified_body["subheadline"]
   article_obj.simple_body = simplified_body["body"]
   article_obj.questions = simplified_body["questions"]
   return render_template("post.html", post=article_obj)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True)
