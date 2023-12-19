from twilio.rest import Client
p={
    "lat":1.352083,
    "lon":103.819839,
    "appid": "0873ea04fff1f2ef4401d7165a18c111",
    "cnt": 4,
}
account_sid="AC9266583bb89ec796c89b0b13a355b3b5"
auth_token="6f3fabd20e8e7c52d851a759fbd57ec3"
number = +12028166416

import requests
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=p)
data = response.json()
#print(data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in data["list"]:
    condition = hour_data["weather"][0]["id"]
    if int(condition)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "It is going to be raining today. Bring an umbrella",
        from_ = '+12028166416',
        to = '+6596625805'
    )
    print(message.status)