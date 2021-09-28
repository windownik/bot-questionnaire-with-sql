from aiogram import types
from main import dp
from aiogram.dispatcher import FSMContext
from modules.dispatcher import answer_Form
from modules.keyboards import kb_2, kb_3, kb_4, kb_5_6, kb_7, kb_8, kb_10, kb_11, kb_12
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Question 2
@dp.message_handler(state=answer_Form.answer_1)
async def start_menu(message: types.Message):
    if 'От 18 до 35 лет' in message.text:
        await message.answer(text='Ваше семейное положение:', reply_markup=kb_2)
        await answer_Form.answer_2.set()
    elif 'До 18 лет' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    elif 'После 35 лет' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 3
@dp.message_handler(state=answer_Form.answer_2)
async def start_menu(message: types.Message):
    if 'Замужем' in message.text:
        await message.answer(text='У вас есть дети?', reply_markup=kb_3)
        await answer_Form.answer_3.set()
    elif 'Не замужем' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 4
@dp.message_handler(state=answer_Form.answer_3)
async def start_menu(message: types.Message):
    if '1 ребенок' in message.text or '2 ребенка' in message.text or '3 и более детей' in message.text:
        await message.answer(text='Возраст младшего ребёнка?', reply_markup=kb_4)
        await answer_Form.answer_4.set()
    elif 'Нет' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 5
@dp.message_handler(state=answer_Form.answer_4)
async def start_menu(message: types.Message):
    if 'От 0 до 3 лет' in message.text or 'От 4 до 7 лет' in message.text or 'От 7 до 14 лет' in message.text:
        await message.answer(text='Согласны ли Вы, что воспитание детей — это настоящая, сложная работа?',
                             reply_markup=kb_5_6)
        await answer_Form.answer_5.set()
    elif 'Старше 14 лет' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 6
@dp.message_handler(state=answer_Form.answer_5)
async def start_menu(message: types.Message):
    if 'Да' in message.text:
        await message.answer(text='У Вас есть потребность во внимании мужа/окружающих?',
                             reply_markup=kb_5_6)
        await answer_Form.answer_6.set()
    elif 'Нет' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 7
@dp.message_handler(state=answer_Form.answer_6)
async def start_menu(message: types.Message):
    if 'Да' in message.text:
        await message.answer(text='Какая из Ваших базовых потребностей удовлетворяются не в полной мере?\n\n'
                                  'Если вашей потребности нет в списке напишите ее.',
                             reply_markup=kb_7)
        await answer_Form.answer_7.set()
    elif 'Нет' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 8
@dp.message_handler(state=answer_Form.answer_7)
async def start_menu(message: types.Message):
    if 'Сон' in message.text or 'Еда' in message.text or 'Безопасность' in message.text or 'Отдых' in message.text\
            or 'Хобби' in message.text or 'Забота' in message.text:
        pass
    await message.answer(text='В какой из перечисленных сфер повседневной жизни Вам требуются перемены?\n\n'
                              'Если вашей необходимой сферы жизни нет в списке напишите ее.',
                         reply_markup=kb_8)
    await answer_Form.answer_8.set()


# Question 9
@dp.message_handler(state=answer_Form.answer_8)
async def start_menu(message: types.Message):
    if 'Отношения' in message.text or 'Отдых' in message.text or 'Режим дня' in message.text or \
            'Материальное состояние' in message.text or 'Эмоциональное состояние' in message.text:
        pass
    await message.answer(text='Укажите от 1 до 3 фраз, отражающих Ваши сокровенные желания/потребности, о которых '
                              'хотелось бы рассказать мужу/окружающим, но по каким-то причинам не можете этого '
                              'сделать. До 5 слов для каждой фразы.', reply_markup=types.ReplyKeyboardRemove())
    await answer_Form.answer_9.set()


# Question 10
@dp.message_handler(state=answer_Form.answer_9)
async def start_menu(message: types.Message):
    await message.answer(text='Вы надели бы футболку с надписью/изображением своего желания?', reply_markup=kb_10)
    await answer_Form.answer_10.set()


# Question 11
@dp.message_handler(state=answer_Form.answer_10)
async def start_menu(message: types.Message):
    if 'Футболка с изображением' in message.text or 'Футболка с текстом' in message.text:
        await message.answer(text='На какой одежде Вы еще хотели бы иметь подобные надписи/изображения?',
                             reply_markup=kb_11)
        await answer_Form.answer_11.set()
    elif 'Не ношу одежду с надписями/изображениями' in message.text:
        await message.answer(text='Спасибо за участие в опросе. Для вас тест закончен.')
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 12
@dp.message_handler(state=answer_Form.answer_11)
async def start_menu(message: types.Message):
    if 'Пижама' in message.text or 'Худи' in message.text or 'Комбинезон' in message.text or 'Спортивные штаны, шорты' \
            in message.text or 'Для всех перечисленных':
        await message.answer(text='В каком ценовом диапазоне Вы готовы рассмотреть покупку подобной одежды?',
                             reply_markup=kb_12)
        await answer_Form.answer_12.set()
    else:
        await message.answer('Нажмите на кнопку в низу')


# Question 12
@dp.message_handler(state=answer_Form.answer_12)
async def start_menu(message: types.Message, state: MemoryStorage):
    if 'От 1000 до 2000 рублей' in message.text or 'От 2000 до 3000 рублей' in message.text or \
            'От 3000 до 4000 рублей' in message.text or '5000 рублей и более' in message.text or \
            'Для всех перечисленных':
        await message.answer(text='Спасибо за прохождение опроса.')
        await state.finish()
    else:
        await message.answer('Нажмите кнопку ниже')
