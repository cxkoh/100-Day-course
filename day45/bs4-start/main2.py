from bs4 import BeautifulSoup
import requests

'''response = requests.get("https://news.ycombinator.com/news")
webpage = response.text
print(webpage)'''

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
header = soup.find_all(name="h3", class_="_h3_cuogz_1")
movies = [movie.getText() for movie in header]
formatted_movies = []
for movie in movies:
    parts = movie.split('.\xa0')
    if len(parts) > 1:
        formatted_movies.append(f"{parts[0]}) {parts[1]}"[:-6])


with open("movie.txt", mode="w") as file:
    for n in formatted_movies:
        file.write(f"{n}\n")

'''url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
print(webpage)
movie_titles = [movies.getText() for movies in all_movies]
print(movie_titles)'''