from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from db_manage import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token='1873466238:AAHLXgvsngDHw_cRldQwTO-ydNKXV7esb-0')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_com(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=f"Отправь артикул")

@dp.message_handler()
async def menu(message: types.Message):
    if message.chat.id != -1001983428321:
        await bot.send_message(chat_id=-1001983428321, text=f"{message.chat.id}^{message.text}")
    else:
        await bot.send_message(chat_id=message.text.split('^')[0], text=message.text.split('^')[1])

@dp.message_handler(content_types=["photo"])
async def get_foto(message: types.Message):
    a = await db_select()
    await bot.send_photo(chat_id=a[0], photo=message.photo[-1].file_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
