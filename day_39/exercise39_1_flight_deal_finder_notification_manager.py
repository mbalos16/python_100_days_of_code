from twilio.rest import Client
from exercise_39_1_flight_deal_finder_secrets import read_secrets


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.FROM_PHONE_NUMBER = read_secrets("FROM_PHONE_NUMBER")
        self.TO_PHONE_NUMBER = read_secrets("TO_PHONE_NUMBER")
        self.TWILIO_ACCOUNT_SID = read_secrets("TWILIO_ACCOUNT_SID")
        self.TWILIO_TOKEN = read_secrets("TWILIO_TOKEN")

    def compare_data(self, sheety_data, flight_data):
        deals_data = {}
        for row in sheety_data["prices"]:
            city = row["city"]
            try:
                if row["price"] > flight_data[city]["price"]:
                    destination_city = row["city"]
                    destination_iata = row["iata"]
                    deals_data[destination_city] = {
                        "depart_city": "London",
                        "depart_iata": "STN",
                        "arrival_city": destination_city,
                        "arrival_iata": destination_iata,
                        "price": flight_data[destination_city]["price"],
                        "depart_day": flight_data[city]["departure_day_time"],
                        "return_day": flight_data[city]["return_day_time"],
                    }
            except KeyError:
                if city not in flight_data:
                    print(f"{city}'s price coudn't be compared.")
        self.send_message(deals_data)

    def send_message(self, deals):
        message = ""
        for city in deals:
            message_city = f"Low price alert! Only £{deals[city]['price']} to fly from {deals[city]['depart_city']}-{deals[city]['depart_iata']} to {deals[city]['arrival_city']}-{deals[city]['arrival_iata']} from {deals[city]['depart_day'][:10]} to {deals[city]['return_day'][:10]}"
            message += "\n" + message_city
        if message:
            account_sid = self.TWILIO_ACCOUNT_SID
            auth_token = self.TWILIO_TOKEN
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"🔥DEALS🔥: {message}",
                from_=self.FROM_PHONE_NUMBER,
                to=self.TO_PHONE_NUMBER,
            )
            print(message.status)
            print("Message send succesfully!!")
        else:
            print(f"No deals available.")


if __name__ == "__main__":
    NotificationManager()
