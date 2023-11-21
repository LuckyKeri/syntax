lst = [1,2,3,4,5,6,7,8,9,10]

# # простой генератор списка 
# a = [x for x in lst]

# for x in lst:
#     a.append(x)

# добавить любое число к каждому элементу lst и сохранить результат в a
# a = [x+5 for x in lst]

# вычесть любое число из каждого элемента lst и сохранить в a
# a = [x-5 for x in lst]

# умножить каждый элемент lst на любое число и сохранить в  a
# a = [x*300 for x in lst]

# # генератор списка с if-условием
# c = [x for x in lst if x>4]

# # второй вариант
# for x in lst:
#     if x > 4:
#         c.append(x)


# генератор списка с вложенным условием if
d = [x for x in lst if x > 4 if x%2 == 0]

# второй вариант 
for x in lst:
    if x > 4:
        if x % 2 == 0:
            d.append(x)
            
print(d)

