import requests
from random import randint

fortuneArr = []

API_URL = "http://localhost:5000/api"  # Change this to your server URL if deployed

try:
    response = requests.get(API_URL)  # Send GET request
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    
    data = response.json()  # Convert response to JSON
    print("Fetched Fortunes from API:")
    for fortune in data:
        fortuneArr.append(fortune['name'])

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")


def returnFortune():
    return fortuneArr[randint(0,(len(fortuneArr)-1))]

