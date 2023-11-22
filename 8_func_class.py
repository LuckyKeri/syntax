# *** функция ***

# создание функции
# не обладает параметрами и ничего не возвращает
def func_1():
    print("hello from Beka")

# обладает параметрами и ничего не возвращает
def func_2(par_0, par_1, par_2=5):
    res = par_0 + par_1 + par_2
    print(res)


# Обладает параметрами и возвращает что-то
def func_3(par_1):
    res = par_1 ** 2
    return res

# вызов функции
# func_2(65, 80, 50)
# result = func_3(8)
# print(result)


# *** Классы ***

# создание класса 
class Cat:
    # метод-конструктор
    def __init__(self, name, a):
        # атрибуты
        self.name = name
        self.age = a

    # матод экземпляра - функция объекта данного класса
    def myau(self):
        res = f"Myau-myau! My name is {self.name}! Age = {self.age}."
        print(res)

# создание экземпляров (объектов) класса Cat
c_0 = Cat("Kitty", 1)
c_1 = Cat("Tommy", 3)
c_2 = Cat("Myrka", 2)

# вывоз метода
c_0.myau()
c_1.myau()

# работа с атрибутами 
# c_2.name = "Tommy"
# print(c_2.name)

c_2.myau()

# функции более подробно
# объектно-ориентирование программирование