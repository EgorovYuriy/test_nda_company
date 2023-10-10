import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "rooms": 2,
    "floor": 2,
    "total_floor": 3,
    "total_area": 54.0,
    "living_area": 37.0,
    "kitchen_area": 7.0,
    "district": "ленинский",
    "street": "строителей",
    "house_number": "52"
}

response = requests.post(url, json=data)

print(response.json())

