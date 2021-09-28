from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import logging

with open('modules/telegram_token.txt', 'r') as file:
    telegram_token = file.read()
    file.close()


storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(telegram_token)
dp = Dispatcher(bot, storage=storage)


# Welcome form
class answer_Form(StatesGroup):
    answer_1 = State()
    answer_2 = State()
    answer_3 = State()
    answer_4 = State()
    answer_5 = State()
    answer_6 = State()
    answer_7 = State()
    answer_8 = State()
    answer_9 = State()
    answer_10 = State()
    answer_11 = State()
    answer_12 = State()
