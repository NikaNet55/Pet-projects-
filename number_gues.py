"""Игра угадай случайное число от 1 до 10 которое загадала программа"""
from random import randrange
from sys import exit
from time import sleep


def guess_game(users_answer: int) -> int:  # функция процесса загадывания и угадывания числа.
    # Принимает предположение пользователя, возвращает количество набранных очков
    guess_num = randrange(1, 11, 1)
    user_score = 10
    tryes = 1
    user_answer_vars = []  # список использованных вариантов чтобы исключить повторения
    while users_answer != guess_num and tryes != 10:
        if users_answer is str:
            print('Я загадал число, а не букву. Попробуй ещё раз')
            users_answer = int(input())
        elif 0 > users_answer or users_answer > 10 or users_answer == float():
            print(" Я загадал число от 1, до 10. Твой вариант не подходит.")
            users_answer = int(input())
        elif users_answer in user_answer_vars:
            print('Этот вариант уже был. не забывай что числа')
            for i in user_answer_vars:
                print(i, sep=' ', end=' ')
            print('уже были. Попробуй ещё раз')
            users_answer = int(input())
        else:
            if users_answer > guess_num:
                print('Твоё число слишком большое')
            elif users_answer < guess_num:
                print('Твоё число слишком маленькое')
            user_score -= 1
            tryes += 1
            user_answer_vars.append(users_answer)
            print('Не угадал. Ты ещё можешь получить', user_score, 'очков. Попробуй ещё раз ;)'
                                                                   'Твоя попытка №', tryes)
            users_answer = int(input())
    print(" Ты угадал! Попыток:", tryes, 'Твой счёт', user_score)
    return user_score


total_score = 0
games = 0
print(' Привет! Давай сыграем с тобой в игру. Я загадаю целое число от 1, до 10, а ты попробуешь угадать.'
      '\n Сыграем? Yes(y)/No(n)')
answer = str(input())
while answer.lower() != 'yes' and answer.lower() != 'y' and answer.lower() != 'no' and answer.lower() != 'n':
    print('Ответьте Yes(y)/No(n)')
    answer = str(input())
if answer.lower() == 'yes' or answer.lower() == 'y':
    print(' Я загадал число. Тебе нужно ввести ответ, если он верный ты победил и получаешь 10 очков!\n'
          'А если нет, у тебя будут ещё попытки, пока не получится, но за каждую из них, ты потеряешь одно очко.'
          'Твоя попытка №1.\n Твой ответ:')
    user_answer = int(input())
    total_score += guess_game(user_answer)  # вызов игры и подсчёт набранных очков
    games += 1
    while answer.lower() == 'yes' or answer.lower() == 'y':
        print('Твой общий счёт', total_score, 'к игре №', games,
              '\n Сыграем ещё раз?(Yes(y)/No(no)')
        answer = str(input())
        print('Я снова загадал число.Твоя попытка №1. Твой ответ:')
        user_answer = int(input())
        total_score += guess_game(user_answer)
        games += 1
elif answer.lower() == 'no' or answer.lower() == 'n':
    print('Может быть в другой раз')
    sleep(3)
    exit(0)
