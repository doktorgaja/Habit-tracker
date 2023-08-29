import requests
from datetime import datetime

TOKEN = "okj312o3hpo123j41j2"
USERNAME = "nemanjagajic"
GRAPH_ID = "graph1"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN,

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixels_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

post_pixels_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did u cycle today? :")
}

response = requests.post(url=post_pixels_endpoint, json=post_pixels_params, headers=headers)
print(response.text)

updated_pixel_params = {
    "quantity": "5"
}

updated_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=updated_pixel_endpoint, json=updated_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)


