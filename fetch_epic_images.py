import os
from dotenv import load_dotenv
import requests
from common_functions import fetch_image, get_file_extension

def get_latest_epic_images_info(api_key, count=10):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[:count]

def fetch_epic_images(api_key):
    images_info = get_latest_epic_images_info(api_key)
    for index, image_info in enumerate(images_info):
        date_parts = image_info['date'].split(' ')[0].split('-')
        image_filename = image_info['image']
        url_template = 'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        image_url = url_template.format(year=date_parts[0], month=date_parts[1], day=date_parts[2], image=image_filename) + f'?api_key={api_key}'
        ext = get_file_extension(image_url)
        filename = f'epic_{index}{ext}'
        fetch_image(image_url, 'images', filename)

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    fetch_epic_images(api_key)
