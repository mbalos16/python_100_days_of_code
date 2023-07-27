# Exercise 38.1. Workout tracking
# Link to the NutritionIx Appi: https://www.nutritionix.com/business/api

import requests
from datetime import datetime
import os

# Nutrition access
NUTRITIONIX_ID = os.environ.get('NUTRITIONIX_ID')
NUTRITIONIX_KEY = os.environ.get('NUTRITIONIX_KEY')
QUERY = input("Tell me which exercises you did: ")

# Sheety access
SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')
SHEETY_AUTH = os.environ.get('SHEETY_AUTH')
PROJECT_NAME = "workoutTracking"


# Get the data from the natural language api  based on the exercise done
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
}
exercise_config = {
    "query": QUERY,
    "gender": "female",
    "weight_kg": 85,
    "height_cm": 171,
    "age": 30,
}
response_exercise = requests.post(
    url=exercise_endpoint, json=exercise_config, headers=exercise_headers
)
data = response_exercise.json()

# Add a new row to the spreadsheet document
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/workouts"
now = datetime.now()
sheety_headers = {"Content-Type": "application/json", "Authorization": SHEETY_AUTH}

sheety_config = {
    "workout": {
        "date": now.strftime("%d%m%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["user_input"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    },
}
response_sheety = requests.post(
    url=sheety_endpoint, json=sheety_config, headers=sheety_headers
)
# print(response_sheety.text)
