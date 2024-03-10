import os
from dotenv import load_dotenv
import requests
from common_functions import fetch_image, get_file_extension


def get_apod_images(api_key, count=30):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    apod_images = [item['url'] for item in response.json() if item.get('media_type') == 'image']

    for index, image_url in enumerate(apod_images):
        ext = get_file_extension(image_url)
        filename = f'nasa_{index}{ext}'
        fetch_image(image_url, 'images', filename)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    get_apod_images(api_key)
