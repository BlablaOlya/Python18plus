import re

l = input("Введите свой login: ")
l = l.rstrip().title()
e = input("Введите свой email: ")
e = e.rstrip()

def validate(email_v):
    pattern = re.compile(r"[a-z0-9\._]+@\w+\.\w+")
    valid = pattern.match(email_v)
    if valid:
        return True
    else:
        return False


def save_data(email, login, file_name):
        with open(file_name, 'a', encoding='utf-8') as new:
            new.write("login: " + str(login) + '\n')
            new.write("email: " + str(email) + '\n')


valid = validate(e)
if valid:
    file = input("Введите название файла, куда необходимо сохранить полученные данные: ")
    file += ".txt"
    save_data(e, l, file)
    print("Ваша учетная запись перенесена в БД")
else:
    print("Проверьте свой email")


