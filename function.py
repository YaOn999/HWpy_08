def show_data() -> str:
    '''1. Эта функция показывает содержимое справочника'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book


def new_data() -> None:
    '''2. Добавляет новую информацию в справочник'''
    with open('data.txt', 'a', encoding='utf-8') as file:
        info = input('Введите новые данные (ФИО | телефон): ')
        file.write(f'\n{info}')


def search_data():
    '''3. Ищет запись в справочнике'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        elem = input('Найти: ')
        for i in book:
            if elem in i:
                flFind = True
                return i


def find_number_to_edit():
    '''4.1. Ищет и возвращает позицию'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        flFind = False
        elem = input('Найти запись для редактирования(удаления): ')
        for i in book:
            if elem in i:
                flFind = True
                print(book.index(i), i)
        if flFind == False:
            print('Значение не найдено')
            exit()
        return int(input('Введите номер записи для редактирования(удаления): '))


def edit_data(i_book: int):
    '''4.2. Перезаписывает файл'''
    book = show_data().split('\n')
    with open('data.txt', 'w', encoding='utf-8') as file:
        book[i_book] = input('Отредактируйте запись: ')
        for element in book:
            file.write(element)
            file.write('\n')


def del_data(i_book: int):
    '''5. Удалить по индексу'''
    book = show_data().split('\n')
    with open('data.txt', 'w', encoding='utf-8') as file:
        del book[i_book]
        for element in book:
            file.write(element)
            file.write('\n')
