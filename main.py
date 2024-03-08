import requests
import os
from urllib.parse import urlsplit, unquote
from os.path import splitext
from dotenv import load_dotenv


def get_latest_epic_images_info(api_key, count=10):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    latest_images_info = response.json()[:count]
    return latest_images_info


def create_epic_image_urls(images_info, api_key):
    earth_images = []
    for image_info in images_info:
        date_parts = image_info['date'].split(' ')[0].split('-')
        image_filename = image_info['image']
        url_template = "https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png?api_key={api_key}"
        url = url_template.format(year=date_parts[0], month=date_parts[1], day=date_parts[2], image=image_filename, api_key=api_key)
        earth_images.append(url)
        for index, image_url in enumerate(earth_images):
            ext = get_file_extension(image_url)
            filename = f'earth_{index}{ext}'
            fetch_spacex_last_launch(image_url, 'images', filename)


def get_apod_images(api_key, count=30):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    apod_images = [item['url'] for item in response.json() if item.get('media_type') == 'image']

    for index, image_url in enumerate(apod_images):
        ext = get_file_extension(image_url)
        filename = f'nasa_{index}{ext}'
        fetch_spacex_last_launch(image_url, 'images', filename)


def fetch_spacex_last_launch(url, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f'{path}/{filename}', 'wb') as file:
        response = requests.get(url)
        response.raise_for_status()
        file.write(response.content)


def get_spacex_launch_images():
    try:
        launch_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
        launch_response = requests.get(launch_url)
        launch_response.raise_for_status()
        launch_images = launch_response.json()['links']['flickr']['original']

        for index, image_url in enumerate(launch_images):
            ext = get_file_extension(image_url)
            filename = f'spacex_{index}{ext}'
            fetch_spacex_last_launch(image_url, 'images', filename)

    except requests.exceptions.HTTPError as error:
        print(f"Can't get data from SpaceX: {error}")


def get_file_extension(url):
    path = urlsplit(url).path
    decoded_path = unquote(path)
    _, ext = splitext(decoded_path)
    return ext


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    latest_images_info = get_latest_epic_images_info(api_key)
    epic_image_urls = create_epic_image_urls(
        latest_images_info,
        api_key
    )
    print(epic_image_urls)

    get_spacex_launch_images()

    get_apod_images(api_key, 30)