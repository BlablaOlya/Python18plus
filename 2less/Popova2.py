import random

i = 1
k = 0
win = False
limit = input("Выбер предел рандома: ")
limit = int(limit)

print("Выберете уровень сложности: низкий, средний, высокий")
level = input("уровень: ")
level = str(level)

if level == "низкий":
    k = 12
if level == "средний":
    k = 9
if level == "высокий":
    k = 6

print("У тебя есть " + str(k) + " попыток")

random_number = random.randint(1, limit)

print("Выберите любое число до предела: ")

while i <= k:
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

