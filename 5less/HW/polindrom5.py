def polindrom(word):
    array = list(word)
    print(array)
    array1 = list(reversed(array))
    print(array1)
    if array == array1:
        return True
    else:
        return False


word = str(input("Введите слово: "))
a = polindrom(word)
if a == True:
    print("Полиндром")
else:
    print("Не полиндром")
