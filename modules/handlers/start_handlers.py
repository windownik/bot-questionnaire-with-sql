from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging
from aiogram.dispatcher import FSMContext
from modules.dispatcher import answer_Form
from modules.keyboards import kb_1
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Start menu
@dp.message_handler(commands=['start'], state='*')
async def start_menu(message: types.Message):
    await message.answer(text='Привет! Перед тобой телеграм бот опросник. Для нас важно получить достоверную '
                              'информацию, по этому пожалуйста отвечайте честно.\n\n'
                              'Ваш возраст?', reply_markup=kb_1)
    await answer_Form.answer_1.set()


# Help menu
@dp.message_handler(commands=['help'], state='*')
async def start_menu(message: types.Message):
    await message.answer(text='Привет! Ты попал в Телеграм бот для подачи заявки на заказ выездного бара.\n'
                              'Для отмены всех действий в любой момент нажмите /cancel')


# Cancel all process
@dp.message_handler(state='*', commands=['cancel'])
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await message.reply('Процес отменен. Все данные стерты. Что бы начать все с начала нажми /start',
                        reply_markup=types.ReplyKeyboardRemove())
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
