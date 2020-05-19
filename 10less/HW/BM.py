from simple_benchmark import benchmark
from HW.recur import recur
from HW.cikl import cikl

import matplotlib.pyplot as plt

func = [recur, cikl]
arguments = {}
for i in range(2,5):
    arguments['i'+ str(i)] = i
print(arguments)
arguments_name = 'natural numbers'

aliases = {cikl: "Цикл", recur: "Рекурсия"}
b = benchmark(func, arguments, arguments_name, function_aliases=aliases)
b.plot()
plt.show(b)