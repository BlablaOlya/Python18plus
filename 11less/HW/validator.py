import re


class Validator:
    @staticmethod
    def validate_login(login):
        pattern = re.compile(r"[a-zA-Z\d]")
        valid = pattern.match(login)
        if valid:
            return True
            print("Логин - валидный")
        else:
            return False

    @staticmethod
    def validate_password(password):
        pattern = re.compile(r"[0-9a-zA-Z!@_#$%^&*]{6,25}")
        valid = pattern.match(password)
        if valid:
            return True
            print("Пароль - валидный")
        else:
            return False
