documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name():
    number = input('Введите номер документа: ')
    for data in documents:
        if data.get("number") == number:
            return print(data.get('name'))
    return print('Документа с таким номером нет')


def get_shelf_number():
    number = input('Введите номер документа: ')
    for key in directories:
        if number in directories.get(key):
            return print(key)
    return print('В полках документа с данным номером нет.')


def get_list_doc(documents):
    for doc in documents:
        print(f"{doc['type']} {doc['number']} {doc['name']};")
