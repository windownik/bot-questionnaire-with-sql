from modules import sqLite


def stat(num: int):
    text = f'answer_{str(num)}'
    data = sqLite.read_all(name=text)
    number_of = len(data)
    # Question 1
    if int(num) == 1:
        a = 0
        b = 0
        c = 0
        d = 0
        for i in data:
            if str(i[0]) == 'До 18 лет':
                a += 1
            elif str(i[0]) == 'От 18 до 35 лет':
                b += 1
            elif str(i[0]) == 'После 35 лет':
                c += 1
            else:
                d += 1
        text = f'<b>Ваш возраст:</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'До 18 лет - <b>{a}</b>\n' \
               f'От 18 до 35 лет - <b>{b}</b>\n' \
               f'После 35 лет - <b>{c}</b>\n' \
               f'Нет данных - <b>{d}</b>\n'
        return text
    # Question 2
    elif int(num) == 2:
        a = 0
        b = 0
        d = 0
        for i in data:
            if str(i[0]) == 'Замужем':
                a += 1
            elif str(i[0]) == 'Не замужем':
                b += 1
            else:
                d += 1
        text = f'<b>Ваше семейное положение</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Замужем - <b>{a}</b>\n' \
               f'Не замужем - <b>{b}</b>\n' \
               f'Нет данных - <b>{d}</b>\n'
        return text
    # Question 3
    if int(num) == 3:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        for i in data:
            if str(i[0]) == 'Нет':
                a += 1
            elif str(i[0]) == '1 ребенок':
                b += 1
            elif str(i[0]) == '2 ребенка':
                c += 1
            elif str(i[0]) == '3 и более детей':
                d += 1
            else:
                e += 1
        text = f'<b>У Вас есть дети?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Нет - <b>{a}</b>\n' \
               f'1 ребенок - <b>{b}</b>\n' \
               f'2 ребенка - <b>{c}</b>\n' \
               f'3 и более детей - <b>{d}</b>\n' \
               f'Нет данных - <b>{e}</b>\n'
        return text
    # Question 4
    if int(num) == 4:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        for i in data:
            if str(i[0]) == 'От 0 до 3 лет':
                a += 1
            elif str(i[0]) == 'От 4 до 7 лет':
                b += 1
            elif str(i[0]) == 'От 7 до 14 лет':
                c += 1
            elif str(i[0]) == 'Старше 14 лет':
                d += 1
            else:
                e += 1
        text = f'<b>Возраст младшего ребёнка:</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'От 0 до 3 лет - <b>{a}</b>\n' \
               f'От 4 до 7 лет - <b>{b}</b>\n' \
               f'От 7 до 14 лет - <b>{c}</b>\n' \
               f'Старше 14 лет - <b>{d}</b>\n' \
               f'Нет данных - <b>{e}</b>\n'
        return text
    # Question 5
    if int(num) == 5:
        a = 0
        b = 0
        e = 0
        for i in data:
            if str(i[0]) == 'Да':
                a += 1
            elif str(i[0]) == 'Нет':
                b += 1
            else:
                e += 1
        text = f'<b>Согласны ли Вы, что воспитание детей — это настоящая, сложная работа?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Да - <b>{a}</b>\n' \
               f'Нет - <b>{b}</b>\n' \
               f'Нет данных - <b>{e}</b>\n'
        return text
    # Question 6
    if int(num) == 6:
        a = 0
        b = 0
        e = 0
        for i in data:
            if str(i[0]) == 'Да':
                a += 1
            elif str(i[0]) == 'Нет':
                b += 1
            else:
                e += 1
        text = f'<b>У Вас есть потребность во внимании мужа/окружающих?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Да - <b>{a}</b>\n' \
               f'Нет - <b>{b}</b>\n' \
               f'Нет данных - <b>{e}</b>\n'
        return text
    # Question 7
    if int(num) == 7:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        k = 0
        for i in data:
            if str(i[0]) == 'Сон':
                a += 1
            elif str(i[0]) == 'Еда':
                b += 1
            elif str(i[0]) == 'Безопасность':
                c += 1
            elif str(i[0]) == 'Отдых':
                d += 1
            elif str(i[0]) == 'Хобби':
                e += 1
            elif str(i[0]) == 'Забота':
                f += 1
            else:
                k += 1
        text = f'<b>Какая из Ваших базовых потребностей удовлетворяются не в полной мере?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Сон - <b>{a}</b>\n' \
               f'Еда - <b>{b}</b>\n' \
               f'Безопасность - <b>{c}</b>\n' \
               f'Отдых - <b>{d}</b>\n' \
               f'Хобби - <b>{e}</b>\n' \
               f'Забота - <b>{f}</b>\n' \
               f'Нет данных, или другое - <b>{k}</b>\n'
        return text
    # Question 8
    if int(num) == 8:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        k = 0
        for i in data:
            if str(i[0]) == 'Отношения':
                a += 1
            elif str(i[0]) == 'Отдых':
                b += 1
            elif str(i[0]) == 'Режим дня':
                c += 1
            elif str(i[0]) == 'Материальное состояние':
                d += 1
            elif str(i[0]) == 'Эмоциональное состояние':
                e += 1
            else:
                k += 1
        text = f'<b>В какой из перечисленных сфер повседневной жизни Вам требуются перемены?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Отношения - <b>{a}</b>\n' \
               f'Отдых - <b>{b}</b>\n' \
               f'Режим дня - <b>{c}</b>\n' \
               f'Материальное состояние - <b>{d}</b>\n' \
               f'Эмоциональное состояние - <b>{e}</b>\n' \
               f'Нет данных, или другое - <b>{k}</b>\n'
        return text
    # Question 9
    if int(num) == 9:
        text = f'Для просмотра ответов на данные вопросы скачайте базу данных (/take_db) и просмотрите данные в ' \
               f'ручном режиме (рекомендуем программу SQLite studio), для загрузки Excel файла нажмите /take_excel'
        return text
    # Question 10
    if int(num) == 10:
        a = 0
        b = 0
        c = 0
        d = 0
        k = 0
        for i in data:
            if str(i[0]) == 'Интересен вариант с изображением':
                a += 1
            elif str(i[0]) == 'Интересен вариант с текстом':
                b += 1
            elif str(i[0]) == 'Интересны оба варианта':
                c += 1
            elif str(i[0]) == 'Не ношу одежду с надписями/изображениями':
                d += 1
            else:
                k += 1
        text = f'<b>Вы надели бы футболку с надписью/изображением своего желания?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Интересен вариант с изображением - <b>{a}</b>\n' \
               f'Интересен вариант с текстом - <b>{b}</b>\n' \
               f'Интересны оба варианта - <b>{c}</b>\n' \
               f'Не ношу одежду с надписями/изображениями - <b>{d}</b>\n' \
               f'Нет данных, или другое - <b>{k}</b>\n'
        return text
    # Question 11
    if int(num) == 11:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        k = 0
        for i in data:
            if str(i[0]) == 'Пижама':
                a += 1
            elif str(i[0]) == 'Худи':
                b += 1
            elif str(i[0]) == 'Комбинезон':
                c += 1
            elif str(i[0]) == 'Спортивные штаны, шорты':
                d += 1
            elif str(i[0]) == 'Для всех перечисленных':
                e += 1
            else:
                k += 1
        text = f'<b>На какой одежде Вы еще хотели бы иметь подобные надписи/изображения?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'Пижама - <b>{a}</b>\n' \
               f'Худи - <b>{b}</b>\n' \
               f'Комбинезон - <b>{c}</b>\n' \
               f'Спортивные штаны, шорты - <b>{d}</b>\n' \
               f'Для всех перечисленных - <b>{e}</b>\n' \
               f'Нет данных - <b>{k}</b>\n'
        return text
    # Question 12
    if int(num) == 12:
        a = 0
        b = 0
        c = 0
        d = 0
        k = 0
        for i in data:
            if str(i[0]) == 'От 1000 до 2000 рублей':
                a += 1
            elif str(i[0]) == 'От 2000 до 3000 рублей':
                b += 1
            elif str(i[0]) == 'От 3000 до 4000 рублей':
                c += 1
            elif str(i[0]) == '5000 рублей и более':
                d += 1
            else:
                k += 1
        text = f'<b>В какой из перечисленных сфер повседневной жизни Вам требуются перемены?</b>\n' \
               f'Количество людей прошедших опрос - <b>{number_of}</b>\n' \
               f'От 1000 до 2000 рублей - <b>{a}</b>\n' \
               f'От 2000 до 3000 рублей - <b>{b}</b>\n' \
               f'От 3000 до 4000 рублей - <b>{c}</b>\n' \
               f'5000 рублей и более - <b>{d}</b>\n' \
               f'Нет данных - <b>{k}</b>\n'
        return text



