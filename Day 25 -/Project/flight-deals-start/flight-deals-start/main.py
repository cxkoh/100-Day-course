from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime

date = datetime.now().date()
now = str(date).split("-")
formatted_date = f"{now[2]}/{now[1]}/{now[0]}"
last_date = f"{now[2]}/{(int(now[1])+6)%12}/{now[0]}"

notification_manager = NotificationManager()
data_manager = DataManager()
flightsearch = FlightSearch()
sheet_data = data_manager.get_destination_data()

origin_city = "SIN"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flightsearch.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for destination in sheet_dacdcdta:
    flight = flightsearch.check_flight(
        origin_city,
        destination["iataCode"],
        from_time=formatted_date,
        to_time=last_date
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send(
            f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )


'''
#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()'''
