print("Введи число и получишь таблицу умножения:")
x = int(input())
for i in range (1, x+1):
    for j in range (i, i*x+1, i):
        print(j, end='\t')
    print()

