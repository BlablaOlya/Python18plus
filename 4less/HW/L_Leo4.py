import random

print("Сейчас можно будете ввести слова в нащ словарик")
print("Если хотите остановить ввод слов, напишите q в английском")

slovar = {}

while True:
    key = input("Введите слово на английском\n:").lower().strip()
    if key == 'q':
        break
    value = input("Введите слово на русском\n:").lower().strip()
    slovar[key] = value

print(slovar)
print("Пора потренироваться, ошибок у нас не более 3")

errors = 0
bonus = 0

mixed = list(slovar.keys())
random.shuffle(mixed)

for key in mixed:
    print('Введите значение слова: ' + key)
    answer = input("Вы считаете, что это слово переводится как\n :").lower().strip()
    if slovar[key] == answer:
        bonus += 1
        print("Отлично! Ваш счет составляет: ", bonus)
    elif errors >= 3:
        errors += 1
        print("Game over")
        break
    else:
        errors += 1
        print('Количество ошибок', errors)