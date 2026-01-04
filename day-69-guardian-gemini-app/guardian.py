from dotenv import load_dotenv
import requests
from post import Post
import os

##Keys and URLs
load_dotenv()
GUARDIAN_API = os.getenv("GUARDIAN_API_KEY")
GUARDIAN_CONTENT = "https://content.guardianapis.com/search?"
GUARDIAN_ARTICLE = "https://content.guardianapis.com/"

def get_articles(topic):
   parm_content = {
   "section": topic,
   "order-by": "newest",
   "page-size": "12",
   "show-fields": "trailText,thumbnail",
   "api-key": GUARDIAN_API,
   }
   ## Request for articles
   content_response = requests.get(GUARDIAN_CONTENT, params=parm_content)
   content_response.raise_for_status()
   content_posts = content_response.json()
   results = content_posts["response"]["results"]
   all_content = []
   for result in results:
      current_result = Post.from_guardian_preview(result)
      all_content.append(current_result)
   return all_content

##Request for body
def get_body(article_id):
   parm_article = {
   "show-fields": "body,trailText,thumbnail",
   "api-key": GUARDIAN_API,
   }

   article_response = requests.get(GUARDIAN_ARTICLE + article_id, params=parm_article)
   article_response.raise_for_status()
   article_posts = article_response.json()
   content = article_posts["response"]["content"]
   return Post.from_guardian_content(content)