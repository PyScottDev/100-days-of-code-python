from bs4 import BeautifulSoup
import requests

response = requests.get("http://news.ycombinator.com/news")

y_c = response.text

soup = BeautifulSoup(y_c, "html.parser")

article_tags = soup.select("span.titleline > a")
article_texts = [tag.get_text() for tag in article_tags]
article_links = [tag.get("href") for tag in article_tags]
score_tags = soup.select("span.score")
upvotes = [int(tag.get_text().split()[0]) for tag in score_tags]

#print(article_tags)
print(article_texts[0])
print(article_links[0])
print(upvotes[0])

highest_votes = max(upvotes)
highest_index = upvotes.index(highest_votes)
print(highest_votes)
print(highest_index)
print(article_texts[highest_index])
print(article_links[highest_index])
# with open("day_45_web_scraping/website.html") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")


# all_tags = soup.find_all(name="a")

# # for tag in all_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
# # #print(all_tags)


# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)

# company_url = soup.select_one(selector="#name")
# print(company_url)

# headings = soup.select(".heading")
# print(headings)