# Exercise 45.2. Access Ycombinator with BeautifulSoup

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []


for article in articles:
    text = article.a.getText()
    article_texts.append(text)
    link = article.a.get("href")
    article_links.append(link)

article_upvote = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]
comparator = 0

# Discovering the most voted article.
for element in article_upvote:
    if element >= comparator:
        comparator = element
index = article_upvote.index(comparator)

# print(article_texts)
# print("---------------------------")

# print(article_links)

# print("---------------------------")
# print(article_upvote)

# print("---------------------------")
# print(comparator)
# print(index)

print(
    f" The title of the most voted article is '{article_texts[index]}', the link to the story is: {article_links[index]} , and has: {article_upvote[index]} votes."
)
