import re


class Calculator:

    def add(self, a, b):
        valid = self.is_valid(a, b)
        if valid[0] == False:
            return valid[1]

        action = a + b
        print(action)
        return action

    def sub(self, a, b):
        valid = self.is_valid(a, b)
        if valid[0] == False:
            return valid[1]

        action = a - b
        print(action)
        return action

    def mult(self, a, b):
        valid = self.is_valid(a, b)
        if valid[0] == False:
            return valid[1]

        action = a * b
        print(action)
        return action

    def div(self, a, b):
        valid = self.is_valid(a, b)
        if valid[0] == False:
            return valid[1]

        if b == 0:
            return 'На ноль делить нельзя'

            action = a / b
            print(action)
            return action

    def is_valid(self, a, b):
        pattern = re.compile(r"^\d{1,}$")
        a_valid = pattern.match(str(a))
        b_valid = pattern.match(str(b))
        if a_valid and b_valid:
            return True, ''
        elif not a_valid:
            return False, '1ое число содержит некорректные данные, введите число'
        elif not b_valid:
            return False, '2ое число содержит некорректные данные, введите число'
