import requests
from datetime import datetime
date = datetime.now()
today_date = f"{date.strftime('%d')}/{date.strftime('%m')}/{date.strftime('%Y')}"
sheety = "https://api.sheety.co/7844db22f42dce39910dd95be43de1cc/copyOfMyWorkouts/workouts"
username = 'shanekoh'
projectname = 'Copy of My Workouts'
sheetname= 'workouts'
GENDER = "male"
WEIGHT_KG = '72'
HEIGHT_CM = '178'
AGE = '19'
api_key = "3915bda04a681efb749d663cefd817d9"
app_id = "e9cd01eb"
website= "https://trackapi.nutritionix.com/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
header={
    "x-app-id": app_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.get(website, json=parameters, headers=header)
result = response.json()

now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety, json=sheet_inputs, auth=("shanekoh", "dndnwidnwidm"))

    print(sheet_response.text)


