from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,URL
import guardian
import gemini

#topic = "politics"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
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
   topic_choice = SubmitField("Choose Topic")

@app.route('/', methods=["GET", "POST"])
def home():
   form = TopicForm()
   if form.validate_on_submit():
      topic = form.topic.data
      return redirect(url_for('article_headings', topic=topic))
   return render_template("index.html", form=form)

@app.route('/headings/<topic>')
def article_headings(topic):
   all_content = guardian.get_articles(topic)
   return render_template("headlines.html", all_posts=all_content, topic=topic)

@app.route("/post/<path:article_id>")  
def get_article(article_id):
   article_obj = guardian.get_body(article_id) 
   return render_template("post.html", post=article_obj)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True)
