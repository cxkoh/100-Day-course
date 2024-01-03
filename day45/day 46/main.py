from bs4 import BeautifulSoup
import requests
date = input("Which year do you want to travel to? type the date in YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
#response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-12/")
soup = BeautifulSoup(response.text, "html.parser")
anchor = soup.select("li ul li h3")
songs = [song.getText().strip() for song in anchor]
print(songs)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:3000",
        client_id='0c795bc1090a460497ed03963d333d40',
        client_secret='cb012709f95844299d5361ccd36e6463',
        show_dialog=True,
        cache_path="token.txt",
        username="Chee Xuan",
    )
)
user_id = sp.current_user()["id"]
year= date[:4]
print(year)
spotify_song_uris = []
for n in songs:
    spotify_result = sp.search(q=f"track:{n} year:{year}", type="track")
    print(spotify_result)
    try:
        song_uri = spotify_result['tracks']['items'][0]['uri']
        spotify_song_uris.append(song_uri)
    except:
        print(f"{n} doesn't exist in Spotify. Skipped.")
if date[5] == '0':
    dates = f"{date[:5]}{date[-4:]}"
else:
    dates = date
print(dates)
playlist = sp.user_playlist_create(user=user_id, name=f"{dates} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_song_uris)