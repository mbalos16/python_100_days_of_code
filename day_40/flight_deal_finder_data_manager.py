import requests
import os
from flight_deal_finder_secrets import read_secrets


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.secrets = read_secrets()
        self.SHEETY_USERNAME = self.secrets["SHEETY_USERNAME"]
        self.SHEETY_AUTH = self.secrets["SHEETY_AUTH"]
        self.endpoint = (
            f"https://api.sheety.co/{self.SHEETY_USERNAME}/flightDeals/prices"
        )
        self.SHEETY_USER_USERNAME = self.secrets["SHEETY_USER_USERNAME"]
        self.user_endpoint = (f"https://api.sheety.co/{self.SHEETY_USER_USERNAME}/flightDeals/users")
        self.email_list = []

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
            
    def get_emails(self):
        sheety_endpoint = self.user_endpoint
        sheety_headers = {
            "Content-Type": "application/json",
            "Authorization": self.SHEETY_AUTH,
        }
        response_sheety = requests.get(url=sheety_endpoint, headers=sheety_headers)
        emails = response_sheety.json()
        for row in emails["users"]:
            self.email_list.append(row["email"])
        return self.email_list

if __name__ == "__main__":
    data = DataManager()
    data.get_emails()