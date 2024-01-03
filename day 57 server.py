from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)
gender_url = "https://api.genderize.io/?name="
age_url = "https://api.agify.io/?name="

@app.route("/")
def hello():
    year = datetime.datetime.now().year
    random_num = random.randint(1,10)
    return render_template("website.html",num=random_num, year=year)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(url=f"{gender_url}{name}")
    gender = gender_response.json()["gender"]
    print(gender)
    age_response = requests.get(url=f"{age_url}{name}")
    age = age_response.json()["age"]
    print(age)
    return render_template("guess.html",name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)