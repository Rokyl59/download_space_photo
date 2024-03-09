import os
import time
import random
import argparse
from dotenv import load_dotenv
import telegram


def publish_photos(directory, interval_hours):
    photos = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    random.shuffle(photos)

    while True:
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            bot.send_document(chat_id='@teeestbot_channel', document=open(photo_path, 'rb'))
            time.sleep(interval_hours * 6)
        
        random.shuffle(photos)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN_API')
    bot = telegram.Bot(token=token)
    parser = argparse.ArgumentParser(description='Publish photos to Telegram channel.')
    parser.add_argument('--directory', type=str, help='Directory with photos to publish')
    parser.add_argument('--interval', type=int, default=4, help='Interval between posts in hours')
    args = parser.parse_args()
    publish_photos(args.directory, args.interval)