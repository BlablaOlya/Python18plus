name_of_file = "date.txt"
amount = 0

with open(name_of_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        amount += int(line)
        average = amount / len(lines)
    print("Общая сумма у нас состовляет ", amount)
    print("Среднее у нас получается: ", average)

new_file = input("Введите название файла, куда необходимо сохранить полученные данные: ")
new_file += ".txt"

with open(new_file, 'a', encoding='utf-8') as new:
    new.write("Общая сумма у нас состовляет " + str(amount) + '\n')
    new.write("Среднее у нас получается: " + str(average) + '\n')
