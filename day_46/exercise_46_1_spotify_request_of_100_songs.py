# Exercise 46.1. Spotify requests of 100 songs.

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Keys:
SPOTIFY_ID = "[INTRODUCE YOUR SPOTIFY ID]"
SPOTIFY_SECRET = "[INTRODUCE YOUR SPOTIFY SECRET]"
redirect_url = "http://localhost:8888/callback"

# Get the user year
question = input(
    "Which year do you want to travel to? Please type the date in this format: YYYY-MM-DD:\n"
)

# Get the data based on user year using BeautifulSoup
response = requests.get(f"https://www.billboard.com/charts/hot-100/{question}/#")
billboard_website = response.text
soup = BeautifulSoup(billboard_website, "html.parser")
song_route = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_route]

# Create a new list in spotify with the Spotypy appi and add new items to it.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=redirect_url,
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Maria_Balos",
    )
)

year = question.split("-")[0]
user_id = sp.current_user()["id"]

uris_list = []
for name in song_names:
    song = sp.search(q=f"track:{name} year:{year}", type="track")
    try:
        uri = song["tracks"]["items"][0]["uri"]
        uris_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{question} Billboard 100", public=False
)
sp.playlist_add_items(playlist_id=playlist["id"], items=uris_list)
