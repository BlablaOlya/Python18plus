import random

i = 0
win = False
limit = input("Выбер предел рандома: ")
limit = int(limit)

print("Выберете уровень сложности: низкий, средний, высокий")
level = input("уровень: ")
level = str(level)

random_number = random.randint(1, limit)

if level == "низкий":
    print("У тебя есть 12 попыток")
    while i <= 11:
        print("Выберите любое число до предела: ")
        guess_number = int(input())
        i += 1
        if guess_number < random_number:
            print("Нужно ввести число побольше")
        if guess_number > random_number:
            print("Нужно ввести число поменьше")
        if guess_number == random_number:
            win = True
            break

if level == "средний":
    print("У тебя есть 9 попыток")
    while i <= 8:
        print("Выберите любое число до предела: ")
        guess_number = int(input())
        i += 1
        if guess_number < random_number:
            print("Нужно ввести число побольше")
        if guess_number > random_number:
            print("Нужно ввести число поменьше")
        if guess_number == random_number:
            win = True
            break

if level == "высокий":
    print("У тебя есть 6 попыток")
    while i <= 5:
        print("Выберите любое число до предела: ")
        guess_number = int(input())
        i += 1
        if guess_number < random_number:
            print("Нужно ввести число побольше")
        if guess_number > random_number:
            print("Нужно ввести число поменьше")
        if guess_number == random_number:
            win = True
            break

if win:
    print("Ты выиграл")
else:
    print("В следующий раз повезет :-). Правильный ответ = ", random_number)

