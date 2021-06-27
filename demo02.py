# python运算符
# 算术运算符
# 加(+)减(-)乘(*)除(/)幂(**) 取余（%):除法的余数 取整除(//)：除法的商的整数部分(向下取整)

# a = 30
# b = 4
# add = a + b
# minus = a - b
# mul = a * b
# divide = a / b
# c = a ** b
# d = a % b
# e = a // b
# print(add, minus, mul, divide, c, d, e)

# 比较运算符
# 等于(==), 不等于(!=)...

# 赋值运算符
# 赋值(=), 运算赋值(+=, -=, *=, /=...)

# 逻辑运算符
# 与或非(and, or, not)

# python运算优先级同常识

# while True:
#     age = int(input('猜猜我多大？'))
#     if age < 18:
#         print('小了！再猜！')
#     elif age > 18:
#         print('大了！再猜！')
#     else:
#         print('猜对了！')
#         break

# python循环语句
# while：在给定的判断条件为 true 时执行循环体，否则退出循环体。
# for: 重复执行语句
# 嵌套语句： while和for可以任意相互嵌套

# 循环控制语句
# break: 在语句块执行过程中终止循环，并且跳出整个循环
# continue: 在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
# pass: pass是空语句，是为了保持程序结构的完整性

# numbers = [12, 37, 5, 42, 8, 3]
# even = []
# odd = []
# while len(numbers) > 0:
#     number = numbers.pop()
#     print(number)
#     if(number % 2 == 0):
#         even.append(number)
#     else:
#         odd.append(number)
# print(numbers)
# print(even)
# print(odd)


# for letter in 'Python':
    # print(letter)


# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:
#     print('当前水果：', fruit)


# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
# # print(range(len(fruits)))
#     print('当前水果：', fruits[index])
#     print(index)


# import numpy
# a_list = numpy.arange(0, 10, 1)
# 直接选取元素
# for a in a_list:
#     print(a)
# 按索引选取元素
# for i in range(len(a_list)):
#     print(a_list[i])

