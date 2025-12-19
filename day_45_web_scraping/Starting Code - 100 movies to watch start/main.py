import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(URL)
empire_text = response.text

soup = BeautifulSoup(empire_text, "html.parser")

article_tags = soup.select("h3.title")
#print(article_tags)
article_texts = [tag.get_text() for tag in article_tags]
article_texts.reverse()
## Angela's method: movies_ordered = article_texts[::-1]
#print(article_texts)

with open("day_45_web_scraping/Starting Code - 100 movies to watch start/top_100_movies.txt", mode="a") as f:
    for movie in article_texts:
        f.write(f"{movie}\n")

