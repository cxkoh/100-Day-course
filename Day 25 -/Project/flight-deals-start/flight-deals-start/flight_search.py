from datetime import datetime
from flight_data import FlightData
import requests



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.Country = "PAR"
        self.date = datetime.now().date()
        self.now = str(self.date).split("-")
        self.formatted_date = f"{self.now[2]}/{self.now[1]}/{self.now[0]}"
        self.last_date = f"{self.now[2]}/{(int(self.now[1])+6)%12}/{self.now[0]}"
        self.api_key = "OWz9rxfVKvYvJyLlh1Qs3WyBMopadBn2"
        self.sheety = "https://api.tequila.kiwi.com"
        self.header = {
            "apikey": self.api_key
        }


    def get_destination_code(self,city_name):
        location_endpoint = f"{self.sheety}/locations/query"
        headers = {"apikey": self.api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,headers=headers, params=query)
        print(response.json())
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def check_flight(self, origin_city, destination, from_time, to_time):
        para = {
            "fly_from": origin_city,
            "fly_to": destination,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "SGD"
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=self.header, params=para)
        print(response)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

'''
Country = "PAR"

api_key = "OWz9rxfVKvYvJyLlh1Qs3WyBMopadBn2!"
website = "https://api.tequila.kiwi.com/v2"
para={
    "fly_from": "SIN",
    "fly_to": Country,
    "date_from": formatted_date,
    "date_to": last_date
}
header = {
    "apikey": api_key
}
response = requests.get(website, json=para, headers=header)
result = response.json()

print(response)'''