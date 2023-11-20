# *** Циклы ***

# Оператор while

# бесконечный цикл 
# while True:
#     print("hello!")

# цикл с условием
val_1 = 0

# while val_1 <= 10:
#     print(f"Значение: {val_1}")
#     # инкремент
#     # val_1 = val_1 + 1
#     val_1 += 1

# прерывание цикла по дополнительному условию

# while True:
#     val = input("введите имя: ")
#     if val == "stop":
#         print("Bye-bye!")
#         break 
#     print(f"Привет, {val}!")

# пропуск части кода тела цикл

val_1 = 0

# while val_1 < 20:
#     # 1 кусок кода
#     print(val_1)
#     val_1 += 1

#     if val_1 < 10:
#         continue

#     # 2 кусок кода
#     print("hello")


# Оператор for

# 1. "чтение" значения  из объекта с последовательностью по порядку
# 2. считанное значение присваивает в собственную переменную
# 3. выполняет код тела

lst_0 = [10, 45, 85, 5, 99, 654]

# for v in lst_0:
#     v *= 100
#     print(v)

dict_0 = dict(a=100, b=200, c=300)

# print(dict_0)

# for item in dict_0.items():
#     print(item)

# for k, v in dict_0.items():
#     print(k, v)

# val_1, val_2, val_3 = (100, 200, 300)

# print(val_1, val_2, val_3)

# for k in dict_0.values():
#     print(k)

# класс range()

r = range(-10, 10, 2)

# print(r)

tupl_0 = tuple(r)

# print(tupl_0)

# for v in r:
#     print(v)

# for v in range(5):
#     v += 10
#     print(v)

for _ in range(5):
    print("hello")

# генератор списка (кортежа)
# генератор словаря 