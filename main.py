from math import*
import random

# функция для ввода числа с клавиатуры

def func():
    print(" Введите число больше нуля ")
    var = float(input())
    if var <= 0:
        func()
    else:
       return var


print ("Введите число = ")
var = float(input())        # считываем первое число))
if var <= 0:                # если число меньше нуля, то другая попытка ввода
    func()
else:
    operation = sqrt(abs(var))        # математическая операция над числом
    array = [0] * int(operation)             # создаем нулевой массив


for i in range(int(operation)):         # создаем массив рандомный чисел от -100 до 100
    array[i] = random.randint(-100, 100)


print("корень из", int(var), "=",operation)        # выводим число получившееся при мат. операции
print("массив из", int(operation), "элементов  ", array)            # выводим массив рандомных чисел