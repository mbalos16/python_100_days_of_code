import requests
import os
from exercise_39_1_flight_deal_finder_secrets import read_secrets


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.SHEETY_USERNAME = read_secrets("SHEETY_USERNAME")
        self.SHEETY_AUTH = read_secrets("SHEETY_AUTH")
        self.endpoint = (
            f"https://api.sheety.co/{self.SHEETY_USERNAME}/flightDeals/prices"
        )

    def access_sheet(self):
        sheety_endpoint = self.endpoint
        sheety_headers = {
            "Content-Type": "application/json",
            "Authorization": self.SHEETY_AUTH,
        }
        response_sheety = requests.get(url=sheety_endpoint, headers=sheety_headers)
        sheet_data = response_sheety.json()
        return sheet_data

    def add_a_new_row(self, new_city, iata_code, lowest_price):
        sheety_endpoint = self.endpoint
        sheety_headers = {
            "Content-Type": "application/json",
            "Authorization": self.SHEETY_AUTH,
        }
        sheety_config = {
            "price": {
                "city": new_city,
                "iata": iata_code,
                "price": lowest_price,
            },
        }
        response_sheety = requests.post(
            url=sheety_endpoint, headers=sheety_headers, json=sheety_config
        )

    def update_data(self, data):
        for row in data:
            id = row["id"]
            iata_code = row["iata"]
            sheety_endpoint = os.path.join(self.endpoint, str(id))
            sheety_headers = {
                "Content-Type": "application/json",
                "Authorization": self.SHEETY_AUTH,
            }
            sheety_config = {
                "price": {
                    "iata": iata_code,
                },
            }
            response_sheety = requests.put(
                url=sheety_endpoint, headers=sheety_headers, json=sheety_config
            )


if __name__ == "__main__":
    DataManager()
