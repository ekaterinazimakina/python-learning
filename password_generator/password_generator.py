import random

def information_collect():

    while True:
        counter = input('Сколько паролей вам необходимо?\n')
        if counter.isdigit():
            counter = int(counter)
            break
        else:
            print('Пожалуйста, введите число')

    while True:
        length = input('Укажите длину пароля\n')
        if length.isdigit():
            length = int(length)
            break
        else:
            print('Пожалуйста, введите число')

    while True:
        digit_included = input('Включать ли цифры 0123456789?\n').lower()
        if digit_included in ('да', 'нет'):
            break
        else:
            print('Пожалуйста, ответьте Да или Нет')

    while True:
        letter_included = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n').lower()
        if letter_included in ('да', 'нет'):
            break
        else:
            print('Пожалуйста, ответьте Да или Нет')

    while True:
        lower_letter_included = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n').lower()
        if lower_letter_included in ('да', 'нет'):
            break
        else:
            print('Пожалуйста, ответьте Да или Нет')

    while True:
        symbols_included = input('Включать ли символы !#$%&*+-=?@^_?\n').lower()
        if  symbols_included in ('да', 'нет'):
            break
        else:
            print('Пожалуйста, ответьте Да или Нет')

    while True:
        strange_symbols_included = input('Исключать ли неоднозначные символы il1Lo0O?\n').lower()
        if strange_symbols_included in ('да', 'нет'):
            break
        else:
            print('Пожалуйста, ответьте Да или Нет')

    return counter, length, digit_included, letter_included, lower_letter_included, symbols_included, strange_symbols_included

def password_generator(counter, length, digit_included, letter_included, lower_letter_included, symbols_included, strange_symbols_included):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''

    if digit_included == 'да':
        chars += digits
    
    if letter_included == 'да':
        chars += uppercase_letters

    if lower_letter_included == 'да':
        chars += lowercase_letters

    if symbols_included == 'да':
        chars += punctuation

    if strange_symbols_included == 'да':
        for symbol in 'il1Lo0O':
            chars = chars.replace(symbol, '')

    if chars == '':
        print('Не выбран ни один набор символов')
        return
    
    while counter > 0:
        password = ''
        for i in range (length):
            password += random.choice(chars) 
        print(password)    
        counter -= 1

data = information_collect()
password_generator(*data)