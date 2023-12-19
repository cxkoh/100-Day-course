import smtplib

import requests
from datetime import *
import time
def is_iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response1.status_code)

    longitude = response1.json()["iss_position"]["longitude"]
    latitude = response1.json()["iss_position"]["latitude"]
    print(longitude)
    print(latitude)
    if 1.352083-5 <= latitude <= 1.352083+5 and 103.819839-5 <= longitude <= 103.819839+5:
        return True

def is_night():

    parameter = {
        "lat":1.352083,
        "lng":103.819839,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    timenow = str(datetime.now().time())
    time_now = int(timenow[:2])
    if time_now  >= sunset or time_now <= sunrise:
        return True
import smtplib
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login("kohcheexuan@gmail.com", "ltjqanxevewvbsxt")
        connection.sendmail(
            from_addr="kohcheexuan@gmail.com",
            to_addrs="kohcheexuan@gmail.com",
            msg= "Subject:look up\n\nThe ISS is above you in the sky"
        )




