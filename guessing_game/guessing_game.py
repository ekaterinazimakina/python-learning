import random
import math

def get_range(): # Get and validate the range
    while True:
        print('Please enter the start and end of the range. Both numbers must be positive integers.')

        a = input()
        b = input()

        if a.isdigit() and b.isdigit():
            a, b = int(a), int(b)

            if a > b:
                print('The first number must be less than the second.')

            elif a == b:
                print('The start and end of the range cannot be the same.')

            else:
                return a, b

        else:
            print('Please enter positive integers.')

def guessing(a, b):
    num = random.randint(a, b)
    return num

def get_difficulty(a, b):
    while True:
        difficulty = input('Choose a difficulty level:\n1 - Easy\n2 - Medium\n3 - Hard\n')
        minimum_attempts = int((math.ceil(math.log2(b - a + 1))))

        if difficulty == '1':
            attempts = int(minimum_attempts * 2)
            print(f'Selected difficulty level: Easy.\nThe number of attempts: {attempts}.')
            return attempts

        elif difficulty == '2':
            attempts = int(minimum_attempts * 1.25)
            print(f'Selected difficulty level: Medium.\nThe number of attempts: {attempts}.')
            return attempts

        elif difficulty == '3':
            attempts =  minimum_attempts
            print(f'Selected difficulty level: Hard.\nThe number of attempts: {attempts}.')
            return attempts

        else:
            print('Please answer 1, 2, or 3.')

def play_game():

    print('Welcome to the number guessing game.')

    while True:

        a, b = get_range()
        num = guessing(a, b)
        attempts = get_difficulty(a, b)
        
        print('A number has been chosen. Try to guess it.')

        counter = 0
        
        while attempts > 0:
            n = input()

            if not n.isdigit():
                print('Please enter positive integers.')
                continue

            n = int(n)

            if n > b or n < a:
                print(f'Your number is out of range. Please enter a number within the range from {a} to {b}')
                continue

            counter += 1
            
            if n == num:
                print('You guessed it! Congratulations!', f'Number of attempts: {counter}', sep='\n')
                break

            attempts -= 1

            if n < num:
                print(f'Your number is less than the chosen one. Try again.\nAttempts left: {attempts}')

            elif n > num:
                print(f'Your number is greater than the chosen one. Try again.\nAttempts left: {attempts}')

        else:
            print(f'Game over! The number was {num}.')
            
        while True:
            answer = input('Do you want to play again? Yes/No.\n').lower()

            if answer == 'yes':
                break

            elif answer == 'no':
                print('Thank you for playing the number guessing game. See you next time.')
                return

            else:
                print('Please answer Yes or No.')

play_game()