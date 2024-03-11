import os
from dotenv import load_dotenv
import requests
from common_functions import fetch_image, get_file_extension
from urllib.parse import urlencode


def fetch_recent_epic_image_metadata(api_key, count=10):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[:count]


def download_and_save_epic_images(api_key, epic_images_metadata):
    date_parts = image_info['date'].split(' ')[0].split('-')
    image_filename = image_info['image']
    url_template = 'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        
    params = {'api_key': api_key}
    encoded_params = urlencode(params)

    image_url = url_template.format(year=date_parts[0], month=date_parts[1], day=date_parts[2], image=image_filename) + '?' + encoded_params
    ext = get_file_extension(image_url)
    filename = f'epic_{index}{ext}'
    fetch_image(image_url, 'images', filename)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    epic_images_metadata = fetch_recent_epic_image_metadata(api_key)

    for index, image_info in enumerate(epic_images_metadata):
        download_and_save_epic_images(api_key, epic_images_metadata)

