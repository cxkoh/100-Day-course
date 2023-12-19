import requests

pixela_endpoint = "https://pixe.la/v1/users"
Username = "shanekohss"
GRAPH_ID = "shanegraph"
Token = "denfnnenewnewnkncewncccwnwns"
para = {
    "token": Token,
    "username": Username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}


graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "token": Token,
    "username": Username,

}
header = {
    "X-USER-TOKEN": Token
}

# response = requests.post(url=pixela_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{Username}/graphs/{GRAPH_ID}"
pixel_data = {
    "date":"20231210",
    "quantity": "6.76"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response.text)