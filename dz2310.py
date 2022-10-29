# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#  list comprehension

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

# map

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# Filter & Lambda 

# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)

# zip

# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = list(zipped_values)
# print(zipped_list)

# emumerate

leters = list('абвгде')
for i, val in enumerate(leters, start=1):
    print(f'№ {i} => {val}')
