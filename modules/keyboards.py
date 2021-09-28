from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_1 = KeyboardButton(f'До 18 лет')
btn_2 = KeyboardButton(f'От 18 до 35 лет')
btn_3 = KeyboardButton(f'После 35 лет')

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_1)
kb_1.add(btn_2)
kb_1.add(btn_3)


btn_4 = KeyboardButton(f'Замужем')
btn_5 = KeyboardButton(f'Не замужем')

kb_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_4)
kb_2.add(btn_5)


btn_6 = KeyboardButton(f'Нет')
btn_7 = KeyboardButton(f'1 ребенок')
btn_8 = KeyboardButton(f'2 ребенка')
btn_9 = KeyboardButton(f'3 и более детей')

kb_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_6)
kb_3.add(btn_7)
kb_3.add(btn_8)
kb_3.add(btn_9)


btn_10 = KeyboardButton(f'От 0 до 3 лет')
btn_11 = KeyboardButton(f'От 4 до 7 лет')
btn_12 = KeyboardButton(f'От 7 до 14 лет')
btn_13 = KeyboardButton(f'Старше 14 лет')

kb_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_10)
kb_4.add(btn_11)
kb_4.add(btn_12)
kb_4.add(btn_13)


btn_14 = KeyboardButton(f'Да')
btn_15 = KeyboardButton(f'Нет')

kb_5_6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_14)
kb_5_6.add(btn_15)


btn_16 = KeyboardButton(f'Сон')
btn_17 = KeyboardButton(f'Еда')
btn_18 = KeyboardButton(f'Безопасность')
btn_19 = KeyboardButton(f'Отдых')
btn_20 = KeyboardButton(f'Хобби')
btn_21 = KeyboardButton(f'Забота')

kb_7 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_16)
kb_7.add(btn_17)
kb_7.add(btn_18)
kb_7.add(btn_19)
kb_7.add(btn_20)
kb_7.add(btn_21)


btn_22 = KeyboardButton(f'Отношения')
btn_23 = KeyboardButton(f'Отдых')
btn_24 = KeyboardButton(f'Режим дня')
btn_25 = KeyboardButton(f'Материальное состояние')
btn_26 = KeyboardButton(f'Эмоциональное состояние')

kb_8 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_22)
kb_8.add(btn_23)
kb_8.add(btn_24)
kb_8.add(btn_25)
kb_8.add(btn_26)


btn_27 = KeyboardButton(f'Интересен вариант с изображением')
btn_28 = KeyboardButton(f'Интересен вариант с текстом')
btn_29 = KeyboardButton(f'Интересны оба варианта')
btn_29_1 = KeyboardButton(f'Не ношу одежду с надписями/изображениями')

kb_10 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_27)
kb_10.add(btn_28)
kb_10.add(btn_29)
kb_10.add(btn_29_1)


btn_30 = KeyboardButton(f'Пижама')
btn_31 = KeyboardButton(f'Худи')
btn_32 = KeyboardButton(f'Комбинезон')
btn_33 = KeyboardButton(f'Спортивные штаны, шорты')
btn_34 = KeyboardButton(f'Для всех перечисленных')

kb_11 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_30)
kb_11.add(btn_31)
kb_11.add(btn_32)
kb_11.add(btn_33)
kb_11.add(btn_34)


btn_35 = KeyboardButton(f'От 1000 до 2000 рублей')
btn_36 = KeyboardButton(f'От 2000 до 3000 рублей')
btn_37 = KeyboardButton(f'От 3000 до 4000 рублей')
btn_38 = KeyboardButton(f'5000 рублей и более')

kb_12 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_35)
kb_12.add(btn_36)
kb_12.add(btn_37)
kb_12.add(btn_38)
