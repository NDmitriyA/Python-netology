month = input('Введите месяц: ')
month = month.lower()
day = int(input('Ведите день: '))
if month == 'март':
    if day >= 21:
        zodiac_sign = 'Овен'
    else:
        zodiac_sign = 'Рыбы'
elif month == 'апрель':
    if day >= 21:
        zodiac_sign = 'Телец'
    else:
        zodiac_sign = 'Овен'
elif month == 'май':
    if day >= 22:
        zodiac_sign = 'Близнецы'
    else:
        zodiac_sign = 'Телец'
elif month == 'июнь':
    if day >= 22:
        zodiac_sign = 'Рак'
    else:
        zodiac_sign = 'Близнецы'
elif month == 'июль':
    if day >= 23:
        zodiac_sign = 'Лев'
    else:
        zodiac_sign = 'Рак'
elif month == 'август':
    if day >= 24:
        zodiac_sign = 'Дева'
    else:
        zodiac_sign = 'Лев'
elif month == 'сентябрь':
    if day >= 23:
        zodiac_sign = 'Весы'
    else:
        zodiac_sign = 'Дева'
elif month == 'октябрь':
    if day >= 24:
        zodiac_sign = 'Скорпион'
    else:
        zodiac_sign = 'Весы'
elif month == 'ноябрь':
    if day >= 23:
        zodiac_sign = 'Стрелец'
    else:
        zodiac_sign = 'Скорпион'
elif month == 'декабрь':
    if day >= 22:
        zodiac_sign = 'Козерог'
    else:
        zodiac_sign = 'Стрелец'
elif month == 'январь':
    if day >= 21:
        zodiac_sign = 'Водолей'
    else:
        zodiac_sign = 'Козерог'
elif month == 'февраль':
    if day >= 19:
        zodiac_sign = 'Рыбы'
    else:
        zodiac_sign = 'Водолей'
print(zodiac_sign)
