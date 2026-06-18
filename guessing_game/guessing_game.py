import random


def get_range():
    while True:
        print('Введите начало и конец диапазона. Начало и конец диапазона должны быть целыми положительными чсилами')

        a = input()
        b = input()

        if a.isdigit() and b.isdigit():
            a, b = int(a), int(b)

            if a > b:
                print('Первое число должно быть меньше второго')

            elif a == b:
                print('Начало и конец диапазона не могут совпадать')

            else:
                return a, b

        else:
            print('Пожалуйста, введите целые положительные числа')


def guessing(a, b):
    num = random.randint(a, b)
    counter = 0

    print('Число загадано. Попробуйте отгадать')

    while True:
        n = input()

        if not n.isdigit():
            print('Пожалуйста, введите число')
            continue

        n = int(n)
        counter += 1

        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')

        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')

        else:
            print('Вы угадали, поздравляем!', f'Количество попыток: {counter}', sep='\n')
            return


def game():
    print('Добро пожаловать в числовую угадайку')

    while True:
        a, b = get_range()
        gessing(a, b)

        while True:
            answer = input('Хотите сыграть ещё раз? Да/Нет\n').lower()

            if answer == 'да':
                break

            elif answer == 'нет':
                print('Спасибо, что играли в числовую угадайку. Ещё увидимся')
                return

            else:
                print('Пожалуйста, ответьте Да или Нет')

game()