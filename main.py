import os
import requests
from dotenv import load_dotenv

# Load the environment variables from .env
load_dotenv()

api_key = os.getenv('API_KEY')

if api_key is not None:
    print(f"API Key: {api_key}")
else:
    print("API_KEY environment variable is not set.")
    exit()


url = 'https://api.nasa.gov/planetary/apod'

parameters = {
    'api_key': api_key,
    'date': '2022-02-22',
    'thumbs': True,
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    print(data)
    date = data['date']
    image_url = data['hdurl']
    image_extension = os.path.splitext(image_url)[1]

    image_filename = os.path.join('images', f'{date}{image_extension}')

    if not os.path.exists(image_filename):
        with open(image_filename, 'wb') as f:
            f.write(requests.get(image_url).content)

        print(f"Image saved as: {image_filename}")
    else:
        print(f"Image for date {date} already exists. Skipping download.")

else:
    print(f"Request failed with the status code: {response.status_code}")


#save the image
