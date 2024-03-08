import telegram
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv('TELEGRAM_TOKEN_API')
bot = telegram.Bot(token=token)


print(bot.get_me())

bot.send_message(text='Hi John!', chat_id='@teeestbot_channel')
