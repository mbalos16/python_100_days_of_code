# Exercise 45.3. 100 movies to watch

from bs4 import BeautifulSoup
import requests

contents = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_website = response.text
soup = BeautifulSoup(empire_website, "html.parser")

# https://www.empireonline.com/movies/features/best-movies-2/
# The page was not working properly so I had to donload it and work on local.
# If doesn't work in the future just uncoment the next code:

# with open("day_45/exercise_45_3_one_hundred_movies_website.html", "r") as f:
#     contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

movie_title = [movie.getText().split(") ") for movie in soup.find_all("h3")]
movie_title_int = [[int(movie[0]), movie[1]] for movie in movie_title]
movie_title_int.reverse()

with open("day_45/exercise_45_3_movies_list.txt", "w") as file:
    for movie in movie_title_int:
        file.write(f"{movie[0]}.{movie[1]}\n")
