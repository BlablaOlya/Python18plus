def calculator(a, b, action):
    if action == "+":
        c = a + b
    elif action == "-":
        c = a - b
    elif action == "*":
        c = a * b
    elif action == "/":
        c = a / b

    return c


while True:
    a = int(input("Введите 1ое число: "))
    b = int(input("Введите 2ое число: "))
    action = input("Выберите действие: +, -, *, /: ")

    d = calculator(a, b, action)
    print(d)
    if input() == "exit":
        break
