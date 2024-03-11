import os
from urllib.parse import urlsplit, unquote
from os.path import splitext
import requests


def get_file_extension(url):
    path = urlsplit(url).path
    decoded_path = unquote(path)
    _, ext = splitext(decoded_path)
    return ext


def fetch_image(url, path, filename, params=None):
    os.makedirs(path, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    content = response.content
    with open(f'{path}/{filename}', 'wb') as file:
        file.write(content)
