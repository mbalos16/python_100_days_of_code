# Exercise 39.1. Flight Deal Finder
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from exercise39_1_flight_deal_finder_notification_manager import NotificationManager
from exercise39_1_flight_deal_finder_flight_search import FlightSearch
from exercise39_1_flight_deal_finder_flight_data import FlightData
from exercise39_1_flight_deal_finder_data_manager import DataManager

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Communicate with the flight Search API
flight_search = FlightSearch()

# Communicate with the spreadsheet
sheet_data = DataManager()

# Comunicate with the Kiwi Tequila API
flight_data = FlightData()

# Comunicate with the Twilio API
notification = NotificationManager()

# Check if there is any empty iataCodes in the spreadsheet and complete them
def fill_empty_iata_codes(data):
    row_nr = 0
    for row in data["prices"]:
        if row.get("iata") == "":
            city = row["city"]
            provided_iata_code = flight_search.get_iata_codes(city)
            data["prices"][row_nr]["iata"] = provided_iata_code
        row_nr += 1
    return data["prices"]

sheety_data = sheet_data.access_sheet()
# Fill the empty iata codes with the coresponding code
data = fill_empty_iata_codes(sheety_data)

# Update the data in the spreadsheet
sheet_data.update_data(data)

# Define the start_date and end_date for the flights
start_date = str(datetime.now() + timedelta(hours=24)).split()[0]
end_date = str(datetime.now() + timedelta(hours=24) + relativedelta(months=+6)).split()[0]

# Get the price for the desired data
flight_data = flight_data.find_flights(data, start_date, end_date=end_date)

# Compare the price from the spreadsheet and the one provided by kiwi tequila
notification.compare_data(sheety_data=sheety_data, flight_data=flight_data)