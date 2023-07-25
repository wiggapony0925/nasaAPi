import requests
import os
from dotenv import load_dotenv

# load the env
load_dotenv()

key = os.getenv("API_KEY")
url = 'https://api.nase.gov/planetary/apod'

parameters = {
    'api key': key,
    'data': '2022-2-22',
    'start_date': "2022-2-20",
    'end_date': '2022-2-22',
    'count': 5,
    'thumbs': True,
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"request failed with the status code: {response.status_code}")