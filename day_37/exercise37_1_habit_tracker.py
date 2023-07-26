# exercise 37.1 Habit tracker with PIXE.LA appi

# The PIXE.LA appi was used to create this project: https://docs.pixe.la/ 
# Check the graph at: https://pixe.la/v1/users/mbalos/graphs/graph1.html

import requests
from datetime import datetime

USERNAME = "[INSERT PIXE.LA USERNAME HERE]"
TOKEN = "[INSERT PIXE.LA TOKEN HERE]"
GRAPH_ID = "[INSERT PIXE.LA GRAPH ID HERE]"

# When a data from a certain day needs to be modify, that date needs to be actualized here in yyyyMMdd format
# DATE_TO_MODIFY = "20230725"

# Create an username and token
pixela_endpoint = "https://pixe.la/v1/users"
# user_param = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url = pixela_endpoint, json = user_param)
# print(response.text)

# Create a graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Reading Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "momiji",}
headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Add a pixl to the graph
pixl_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# today = datetime(year=2023, month=7, day=24) if we want to add a pixl for another today
pixl_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours have you read today?\n"),
}
response_pixl = requests.post(url=pixl_endpoint, json=pixl_config, headers=headers)
print(response_pixl.text)


# # Modify a pixl in an existing day in the graph
# pixl_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TO_MODIFY}"
# pixl_update_config = {
#     "quantity": "7",
# }
# response_pixl_update = requests.put(
#     url=pixl_endpoint, json=pixl_update_config, headers=headers
# )
# print(response_pixl_update.text)


# Delete a pixl in an existing day in the graph
# pixl_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TO_MODIFY}"
# response_pixl_update = requests.delete(
#     url=pixl_endpoint, headers=headers
# )
# print(response_pixl_update.text)