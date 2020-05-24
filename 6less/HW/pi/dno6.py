name_of_file = "pi_million_digits.txt"
print("Пришло время узнать, есть ли Ваша дата рождения в трансцендентном числе Pi")
birth = input("Введите дату Вашего рождения: ")
a = False
with open(name_of_file, encoding='utf-8') as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        i += 1
        if birth in line:
            a = True
            break

if a:
    print("Здорово! Вы в числе PI.")
    print("Вы находитесь в ", i, "-ой строке")
else:
    print("В числе PI не рождаются.")
