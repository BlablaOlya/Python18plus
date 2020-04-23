import random

numbers = list(range(0, 1))
print("Ваш вид ставки: внутренняя, на цвет, на дюжину")

bet_type = input()
inside_bet = "внутренняя"
color_bet = "на цвет"
outside_bet = "на дюжину"

print("Ваши ставки, пожалуйста!")
bet = input()
print("Ставки сделаны, ставок больше нет, спасибо!")

x = random.choice(numbers)

if (x % 2) == 0:
    color_x = "черный"
else:
    color_x = "красный"

if 1 < x <= 12:
    dozen = "Первая дюжина"
if 12 < x <= 24:
    dozen = "Вторая дюжина"
if 24 < x <= 36:
    dozen = "Третья дюжина"

if x == 0:
    print("Все деньги в козино")

print(x)
print(color_x)
print(dozen)

if bet_type == inside_bet:
    result = int(bet)
    if result == x:
        print("Ты выиграл!")
    else:
        print("Ты проиграл")

if bet_type == color_bet:
    result = str(bet)
    if result == color_x:
        print("Ты выиграл!")
    else:
        print("Ты проиграл")

if bet_type == outside_bet:
    result = str(bet)
    if result == dozen:
        print("Ты выиграл!")
    else:
        print("Ты проиграл")




