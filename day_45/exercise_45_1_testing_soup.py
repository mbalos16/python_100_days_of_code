# Exercise 45.1. Testing BeautifulSoup
from bs4 import BeautifulSoup

with open("day_45/exercise_45_1_website.html", "r") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

# Print the complete HTML file.
print(soup)

# Print the HTML's title file including tag.
print(soup.title)

# Print the HTML's title file, just the string without tag.
print(soup.title.string)

# Print the HTML's title file, just the tag without string.
print(soup.title.name)

# Print the HTML's list of all the anchor tags
print(soup.find_all(name="a"))

# Print the HTML's list of all the paragraphs tags
print(soup.find_all(name="p"))

# To get just the content from the tags in a list we can apply the getText() method.
anchor_tags = soup.find_all(name="a")
for tag in anchor_tags:
    print(tag.getText())

# To get just the value of some element (eg. href) from a tags, we can apply the get() method.
anchor_tags = soup.find_all(name="a")
for tag in anchor_tags:
    print(tag.get("href"))

# ID can be used to identify items
heading = soup.find(name="h1", id="name")
print(heading)
