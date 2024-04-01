import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command 
from aiogram.types import Message
from config_reader import config

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
# bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@dp.message(Command(commands=['start']))
async def cmd_start(msg: Message):
    user_name = msg.from_user.full_name
    user_id = msg.from_user.id
    text = f'Привет, {user_name}! Я Бот, который переводит с кириллицы на латиницу! Введи слово, которое нужно перевести:'
    logging.info(f"{user_id}:{user_id} - запустил бота")
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def message(msg: Message):
    full_name = msg.text 
    russian = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 
               'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 
               'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 
               'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 
               'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 
               'ъ', 'э', 'ю', 'я', 'ь'] # добавим мягкий знак, так как в танслите МИД его нет)))
    latin = ['A', 'B', 'V', 'G', 'D', 'E', 'E', 'ZH', 'Z', 'I', 'I', 'K', 
             'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'KH', 'TS',
             'CH', 'SH', 'SHCH', 'Y', 'IE', 'E', 'IU', 'IA', 'a', 'b', 'v', 
             'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 
             'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 
             'shch', 'y', 'ie', 'e', 'iu', 'ia', '']
    
    name_translit = ''.join([latin[russian.index(i)] if i in russian else i for i in full_name])
    logging.info(f"input: {full_name}, Converted: {name_translit}")
    await msg.answer(text=name_translit)

if __name__ == '__main__':
    dp.run_polling(bot) 