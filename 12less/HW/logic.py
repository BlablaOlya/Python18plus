from HW.Calculator import Calculator

c = Calculator()

a = int(input("Введите 1ое число: "))
b = int(input("Введите 2ое число: "))
action = input("Выберите действие: +, -, *, /: ")

if action == "+":
    c.add(a, b)
elif action == "-":
    c.sub(a, b)
elif action == "*":
    c.mult(a, b)
elif action == "/":
    c.div(a, b)
