
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7844db22f42dce39910dd95be43de1cc/flightDeal/workouts"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url="https://api.sheety.co/7844db22f42dce39910dd95be43de1cc/flightDeal/workouts")
        data = response.json()
        self.destination_data = data["workouts"]
        return self.destination_data



    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "workouts": {
                    "iataCode": city["iataCode"]
                }
            }
            print(new_data)
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

