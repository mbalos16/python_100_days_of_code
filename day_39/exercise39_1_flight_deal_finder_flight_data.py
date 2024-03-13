import requests
from exercise_39_1_flight_deal_finder_secrets import read_secrets


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, origin="LON", min_nights=7, max_nights=28) -> None:
        self.secrets = read_secrets()
        self.FLIGHT_DATA_ENDPOINT = self.secrets["FLIGHT_DATA_ENDPOINT"]
        self.FLIGHT_DATA_APIKEY = self.secrets["FLIGHT_DATA_APIKEY"]
        self.origin = origin
        self.min_nights = min_nights
        self.max_nights = max_nights

    def find_flights(
        self,
        data,
        start_date,
        end_date,
    ):
        flight_data = {}
        tequila_endpoint = self.FLIGHT_DATA_ENDPOINT
        headers = {
            "accept": "application/json",
            "apikey": self.FLIGHT_DATA_APIKEY,
        }
        for row in data:
            tequila_config = {
                "fly_from": self.origin,
                "fly_to": row["iata"],
                "date_from": start_date,
                "date_to": end_date,
                "one_for_city": 1,
                "nights_in_dst_from": self.min_nights,
                "nights_in_dst_to": self.max_nights,
                "ret_from_diff_city": False,
                "ret_to_diff_city": False,
                "cur": "GBP",
                "max_stopovers": 0,
            }

            response_tequila = requests.get(
                url=tequila_endpoint, headers=headers, params=tequila_config
            )
            each_result = response_tequila.json()
            if each_result["_results"] == 1:
                city_to = each_result["data"][0]["cityTo"]
                price = each_result["data"][0]["price"]
                departure_day_time = each_result["data"][0]["route"][0][
                    "local_departure"
                ]
                return_day_time = each_result["data"][0]["route"][1]["local_departure"]
                flight_data[city_to] = {
                    "price": price,
                    "departure_day_time": departure_day_time,
                    "return_day_time": return_day_time,
                }
            else:
                print(f"{row['city']} has no flights available.")
        return flight_data


if __name__ == "__main__":
    FlightData()
