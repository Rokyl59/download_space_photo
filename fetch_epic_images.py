import os
from dotenv import load_dotenv
import requests
from common_functions import get_file_extension, fetch_image


def fetch_recent_epic_image_metadata(api_key, count=10):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[:count]


def download_and_save_epic_image(api_key, image_info, index):
    date_parts = image_info['date'].split(' ')[0].split('-')
    image_filename = image_info['image']
    url_template = f'https://api.nasa.gov/EPIC/archive/natural/{date_parts[0]}/{date_parts[1]}/{date_parts[2]}/png/{image_filename}.png'
    ext = get_file_extension(url_template)
    filename = f'epic_{index}{ext}'
    fetch_image(url_template, 'images', filename, params={'api_key': api_key})


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    epic_images_metadata = fetch_recent_epic_image_metadata(api_key)
    for index, image_info in enumerate(epic_images_metadata):
        download_and_save_epic_image(api_key, image_info, index)
