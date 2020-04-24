import random

win = False
numbers = list(range(0, 37))
print("Ваш вид ставки: внутренняя, на цвет, на дюжину")

bet_type = input()
inside_bet = "внутренняя"
color_bet = "на цвет"
outside_bet = "на дюжину"

print("Ваши ставки, пожалуйста!")
bet = input()
print("Ставки сделаны, ставок больше нет, спасибо!")

x = random.choice(numbers)

if x in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
    color_x = "красный"
else:
    color_x = "черный"
if x == 0:
    color_x = "-"

if 1 < x <= 12:
    dozen = "первая"
if 12 < x <= 24:
    dozen = "вторая"
if 24 < x <= 36:
    dozen = "третья"
if x == 0:
    dozen = "-"

if x == 0:
    print("Все деньги в козино")

print("Выигрышный результат: ", x)
print("Выигрышный цвет: ", color_x)
print("Выигрышная дюжина: ", dozen)

if bet_type == inside_bet:
    result = int(bet)
    if result == x:
        win = True

if bet_type == color_bet:
    result = str(bet)
    if result == color_x:
        win = True

if bet_type == outside_bet:
    result = str(bet)
    if result == dozen:
        win = True

if win:
    print("Ты выиграл!")
else:
    print("В следующий раз повезет :-)")



