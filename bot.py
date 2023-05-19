import random
from os import system
from datetime import datetime

import requests
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import *
from oop5 import Unsplash 

system("clear")
bot=Bot(token="6018827344:AAH8vgHTa3Ek1piBU93SwbMap1Sd5NwKbWo",parse_mode="HTML")
dp=Dispatcher(bot)

markup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(KeyboardButton(text="Получить фотку"))

class Photo(Unsplash):
    def __init__(self):
        super().__init__()

img=Photo()


@dp.message_handler(commands=["start"])
async def start(message:Message):
    await message.delete()
    await message.answer("Hello, I'm a Telegram bot and I have images",reply_markup=markup)


@dp.message_handler(commands=["photo","image","img","unsplash","png","jpg","jpeg"])
async def command_image(message:Message):
    caption=img.processing_image()
    await message.answer(text=caption)


@dp.message_handler(content_types=ContentType.TEXT)
async def message_handler(message:Message):
    if message.text.lower()=="получить фотку":
        await message.delete()
        caption=img.processing_image()
        await message.answer(text=caption)
    else:
        await message.delete()   


if __name__ == "__main__":
    try:
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemError):
        pass