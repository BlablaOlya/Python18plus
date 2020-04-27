import random
amount_of_words = input("Как много слов вы собираетесь занести в словарь? ")
aow = int(amount_of_words)

slovar = {}

for i in range(aow):
    key = input("Введите слово на английском\n:")
    value = input("Введите слово на русском\n:")
    slovar[key] = value
print(slovar)

mixed = list(slovar.keys())
random.shuffle(mixed)

for key in mixed:
    print('Введите значение слова: ' + key)
    answer = input("Вы считаете, что это слово переводится как\n :")
    if slovar[key] == answer:
        print("Все правильно")
    else:
        print("Бывает")