import argparse
import requests
from common_functions import fetch_image, get_file_extension

def fetch_spacex_launch_images(launch_id=None):
    if launch_id:
        launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        launch_url = 'https://api.spacexdata.com/v5/launches/latest'
    
    response = requests.get(launch_url)
    response.raise_for_status()
    launch_images = response.json()['links']['flickr']['original']

    for index, image_url in enumerate(launch_images):
        ext = get_file_extension(image_url)
        filename = f'spacex_{index}{ext}'
        fetch_image(image_url, 'images', filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download SpaceX launch images.')
    parser.add_argument('--launch_id', type=str, help='The ID of the SpaceX launch.')
    args = parser.parse_args()
    fetch_spacex_launch_images(args.launch_id)