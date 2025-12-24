from flask import Flask, render_template
import requests
from post import Post

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_response.raise_for_status()
blog_posts = blog_response.json()
all_posts = []

for post in blog_posts:
    current_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(current_post)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route("/post/<int:index>")
def get_posts(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)





# @app.route("/blog")
# def get_blog():
#     blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
#     blog_response.raise_for_status()
#     blog_posts = blog_response.json()
#     return render_template("blog.html", blog_posts=blog_posts)



if __name__ == "__main__":
    app.run(debug=True)
