# Задание 1
#1
# x = int(str(float(5))) #выйдет как float
# #2
# x = 'aa' == 'AA' # boolean false
#3
# x = {i: i**2 for i in range(5)} #генератор списков
# #4
# x = set(list((5, 6, 7))) # множества
# #5
# a = {1: 1, 2: 4, 3: 9}
# x = a.get(4)  # None
# #6
# x = [].append('j') # none


# for i in range(10):
#
# 	if i < 5:
#
# 		x = 'hello'
# 	else:
# 		x = 5 # 5 раз выведит hello (int)
# #8
# x = input('Enter and integer: ') # str

# #9
# a = 5
# b = [1, 3, 5, ]
# x = 'x'
# a, b, x = x, a, b #

# #10
# def func(x, y=5):
# 		return x + y
# x = func('Jaguar ', 'hunter') #str

# Задание 2
# def summa(deposit, mesyac, procent ):
#     b = deposit
#     c = 0
#     while b < mesyac:
#         b = procent / 100 / 12 * b + b
#         c += 1
#     return c
# print(summa(100000, 1231231, 12))
# # #



#Задние 3





# def func(*args):
#     lst = args
#
#     for i in range(len(lst)):
#
#         a = {x: y for x in lst for y in range(1 ,4)}
#     return a
#
#
# print(func('x', 5, 'John'))









#
# def func(*args):
#     a = list(args)
#     b = {x: [y for y in range(len(a))] for x in args}
#     b = {}
#     j = 1
#     for i in range(len(a)):
#         b[a[i]] = j
#         j += 1
#     return b
# print(func('x', 5, 'John'))



