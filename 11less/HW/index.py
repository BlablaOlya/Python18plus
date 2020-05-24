from HW.storage import *
from HW.validator import *
from HW.play import *

def greet(answer):

    if answer == 'Нет':
        print("Предлагаю заегистрироваться ")
    elif answer == 'Да':
        quit(0)
    else:
        print("Введите 'да' или 'нет' ")
        quit(0)


answer = input("Вы зарегистрированы в нашей системе? Введите 'да' или 'нет' \n")
greet(answer.strip().title())

login = input("Введите ваш login (используя латинские буквы): \n")
login_valid = Validator.validate_login(login.strip().title())
if login_valid == False:
    quit(0)

password = input("Введите ваш пароль (от 6 до 25 симолов, используя латинские буквы и/или цифры и/или !@_#$%^&*): \n")
password_valid = Validator.validate_password(password.strip())
if password_valid == False:
    quit(0)

user = User(login, password)
Storage.save(user)
board = list(range(1, 10))
Play.main(board)






