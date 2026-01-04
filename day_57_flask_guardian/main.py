from flask import Flask, render_template
import requests
from post import Post
from dotenv import load_dotenv
import os


load_dotenv()
GUARDIAN_API = os.getenv("GUARDIAN_API_KEY")
GUARDIAN_CONTENT = "https://content.guardianapis.com/search?"
GUARDIAN_ARTICLE = "https://content.guardianapis.com/"
topic = "politics"


parm_content = {
   "section": topic,
   "order-by": "newest",
   "page-size": "12",
   "show-fields": "trailText,thumbnail",
   "api-key": GUARDIAN_API,
}


content_response = requests.get(GUARDIAN_CONTENT, params=parm_content)
content_response.raise_for_status()
content_posts = content_response.json()
results = content_posts["response"]["results"]
#print(results)


all_content = []


for result in results:
   current_result = Post(result["id"], result["webTitle"], result["fields"]["trailText"], result["fields"]["thumbnail"], result["sectionId"])
   all_content.append(current_result)


app = Flask(__name__)


@app.route('/')
def home():
   return render_template("index.html", all_posts=all_content, topic=topic)


@app.route("/post/<path:article_id>")
def get_article(article_id):
   parm_article = {
   "show-fields": "body,trailText,thumbnail",
   "api-key": GUARDIAN_API,
   }


   article_response = requests.get(GUARDIAN_ARTICLE + article_id, params=parm_article)
   article_response.raise_for_status()
   article_posts = article_response.json()
   article = article_posts["response"]["content"]
   article_obj = Post(article["id"], article["webTitle"], article["fields"]["trailText"], article["fields"]["thumbnail"], article["fields"]["body"])


   return render_template("post.html", post=article_obj, topic=topic)






if __name__ == "__main__":
   app.run(debug=True)



