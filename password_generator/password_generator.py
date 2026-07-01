import random

def information_collect():

    while True:
        counter = input('How many passwords do you need?\n')
        if counter.isdigit():
            counter = int(counter)
            break
        else:
            print('Please enter a number')

    while True:
        length = input('Enter password length\n')
        if length.isdigit():
            length = int(length)
            break
        else:
            print('Please enter a number')

    while True:
        digit_included = input('Include digits 0123456789? (yes/no)\n').lower()
        if digit_included in ('yes', 'no'):
            break
        else:
            print('Please answer yes or no')

    while True:
        letter_included = input('Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (yes/no)\n').lower()
        if letter_included in ('yes', 'no'):
            break
        else:
            print('Please answer yes or no')

    while True:
        lower_letter_included = input('Include lowercase letters abcdefghijklmnopqrstuvwxyz? (yes/no)\n').lower()
        if lower_letter_included in ('yes', 'no'):
            break
        else:
            print('Please answer yes or no')

    while True:
        symbols_included = input('Include symbols !#$%&*+-=?@^_? (yes/no)\n').lower()
        if  symbols_included in ('yes', 'no'):
            break
        else:
            print('Please answer yes or no')

    while True:
        ambiguous_symbols_included = input('Exclude ambiguous symbols il1Lo0O? (yes/no)\n').lower()
        if ambiguous_symbols_included in ('yes', 'no'):
            break
        else:
            print('Please answer yes or no')

    return counter, length, digit_included, letter_included, lower_letter_included, symbols_included, ambiguous_symbols_included

def password_generator(counter, length, digit_included, letter_included, lower_letter_included, symbols_included, ambiguous_symbols_included):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''

    if digit_included == 'yes':
        chars += digits
    
    if letter_included == 'yes':
        chars += uppercase_letters

    if lower_letter_included == 'yes':
        chars += lowercase_letters

    if symbols_included == 'yes':
        chars += punctuation

    if ambiguous_symbols_included == 'yes':
        for symbol in 'il1Lo0O':
            chars = chars.replace(symbol, '')

    if chars == '':
        print('No character set selected')
        return
    
    while counter > 0:
        password = ''
        for i in range (length):
            password += random.choice(chars) 
        print(password)    
        counter -= 1

data = information_collect()
password_generator(*data)