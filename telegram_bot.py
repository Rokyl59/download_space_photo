import os
import time
import random
import argparse
from dotenv import load_dotenv
import telegram


SECOND_IN_HOUR = 3600


def publish_photos(bot, chat_id, directory, interval_hours):
    photos = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    random.shuffle(photos)

    while True:
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            with open(photo_path, 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            time.sleep(interval_hours * SECOND_IN_HOUR)
        random.shuffle(photos)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN_API')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = telegram.Bot(token=token)
    
    parser = argparse.ArgumentParser(description='Publish photos to Telegram channel.')
    parser.add_argument('--directory', type=str, default='images', help='Directory with photos to publish')
    parser.add_argument('--interval', type=int, default=4, help='Interval between posts in hours')
    args = parser.parse_args()
    
    publish_photos(bot, chat_id, args.directory, args.interval)
