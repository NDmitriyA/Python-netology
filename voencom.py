height = int(input('Ваш рост: '))
age = int(input('Ваш возраст: '))
number_children = int(input('Количество детей: '))
form_training = int(input('Форма обучения "0-не учусь" "1-очно" "2-заочно": '))

if (18 <= age <= 27) and (number_children < 2) and (form_training != 1):
    if height <= 170:
        print('Танковые войска')
    elif height <= 185:
        print('Мотострелки')
    elif height <= 200:
        print('ВДВ')
    else:
        print('Другой род войск')
else:
    print('Не пригоден для службы')
