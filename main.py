import os
import logging
import time

import requests
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.environ['API_TOKEN']
URL = 'https://www.ikea.com/ru/ru/'
WATCH_PHRASE = 'Прием новых заявок запустится немного позже.'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def watch(message: types.Message):
    s = requests.Session()
    await message.answer('Watching site changes...')
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    while True:
        resp = s.get(URL, headers=headers)
        if WATCH_PHRASE not in resp.text:
            await message.answer('Form available. Visit https://www.ikea.com/ru/ru/')
            break
        time.sleep(15)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
