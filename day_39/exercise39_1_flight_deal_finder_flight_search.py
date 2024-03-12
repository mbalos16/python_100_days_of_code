import requests
from exercise_39_1_flight_deal_finder_secrets import read_secrets


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.FLIGHT_SEARCH_ENDPOINT = read_secrets("FLIGHT_SEARCH_ENDPOINT")
        self.FLIGHT_SEARCH_APIKEY = read_secrets("FLIGHT_SEARCH_APIKEY")

    def get_iata_codes(self, city):
        tequila_endpoint = self.FLIGHT_SEARCH_ENDPOINT
        headers = {
            "accept": "application/json",
            "apikey": self.FLIGHT_SEARCH_APIKEY,
        }

        tequila_config = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true",
        }

        response_tequila = requests.get(
            url=tequila_endpoint, headers=headers, params=tequila_config
        )
        response_tequila = response_tequila.json()
        iata = response_tequila["locations"][0]["code"]
        return iata


if __name__ == "__main__":
    FlightSearch()
