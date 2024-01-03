import requests
gender_url = "https://api.genderize.io/?name="

gender_response = requests.get(url=f"{gender_url}koh")
gender = gender_response.json()["gender"]
print(gender)