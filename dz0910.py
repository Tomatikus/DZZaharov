# Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = int(input())
 
# suma = 0
 
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     n = n // 10
 
# print("Сумма:", suma)


# Задача 2: Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from math import factorial

# n = int(input('Введите число: '))
# f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
# list2 = list( f(i) for i in range(1, n +1))
# print(list2)


# Задача 5: Реализуйте алгоритм перемешивания списка.

# import random 
# listA = [2, 8, 4, 3, 1, 5]
# random.shuffle(listA)
# print(listA)

# Задача 3:Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран 
# их сумму.

# print('Введите число')
# n = int(input())
# lst = [round((1+1/n)**n) for n in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')


# Задача 4:Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

