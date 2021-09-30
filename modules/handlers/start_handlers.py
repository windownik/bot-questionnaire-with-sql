from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging, sqlite3
import openpyxl
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, answer_Form
from modules.keyboards import kb_2
from modules import stat_work, sqLite


# Start menu
@dp.message_handler(commands=['start'], state='*')
async def start_menu(message: types.Message):
    await message.answer(text='Ваше семейное положение?', reply_markup=kb_2)
    data = sqLite.read_values_by_name(data=message.from_user.id)
    if data is None:
        sqLite.insert_first_note(telegram_id=message.from_user.id)
    else:
        pass
    await answer_Form.answer_2.set()


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


# Take data base
@dp.message_handler(commands=['take_excel'], state='*')
async def start_menu(message: types.Message):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    curs.execute(f'SELECT * FROM answers')
    data = curs.fetchall()
    xl = openpyxl.load_workbook(filename='modules/Output.xlsx')
    worksheet = xl['1']
    line = 1
    for i in data:
        worksheet[f'B{line}'] = f'{i[2]}'
        worksheet[f'C{line}'] = f'{i[3]}'
        worksheet[f'D{line}'] = f'{i[4]}'
        worksheet[f'E{line}'] = f'{i[5]}'
        worksheet[f'F{line}'] = f'{i[6]}'
        worksheet[f'G{line}'] = f'{i[7]}'
        worksheet[f'H{line}'] = f'{i[8]}'
        worksheet[f'I{line}'] = f'{i[9]}'
        worksheet[f'J{line}'] = f'{i[10]}'
        worksheet[f'K{line}'] = f'{i[11]}'
        worksheet[f'L{line}'] = f'{i[12]}'
        worksheet[f'M{line}'] = f'{i[13]}'
        line += 1
    xl.save('modules/Output.xlsx')
    xl.close()
    with open('modules/Output.xlsx', 'rb') as file:
        await bot.send_document(chat_id=message.from_user.id, document=file, caption='Отправил')
    file.close()


# Take data base
@dp.message_handler(commands=['take_db'], state='*')
async def start_menu(message: types.Message):
    chat_id = message.from_user.id
    with open('modules/database.db', 'rb') as file:
        await bot.send_document(chat_id=chat_id, document=file, caption='Отправил')
    file.close()


# Get data
@dp.message_handler(state='*', commands=['stata'])
async def cancel_handler(message: types.Message):
    await message.answer('Введите номер вопроса от 1 до 12')
    await answer_Form.stata_1.set()


@dp.message_handler(state=answer_Form.stata_1)
async def cancel_handler(message: types.Message):
    if message.text.isdigit():
        if 0 < int(message.text) < 13:
            text = stat_work.stat(message.text)
            await message.answer(text=text, parse_mode='html')
        else:
            await message.answer('Введите только число от 1 до 12')
    else:
        await message.answer('Введите только число от 1 до 12')
