# python有交互式和脚本式两种编码方式

# 标识符（a1,v2）不能以数字开头

# python的保留字符有既定含义，不能用来自定义（如：print，and）

# python相同的缩进空白数量代表同一级命令，缩进越少，优先级越高

# python一般以新行作为语句的结束符（可以使用斜杠（ \）将一行的语句分为多行显示）
# a = 1 + 1 \
# + 1
# print(a)

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。
# a = [1, 2, 3, 
# 4]
# print(a)

# 同一命令里单双引号要混合使用
# print('我的外号叫"xiaozhu"')

# 注释
# 行注释： #
# 块注释： 
# '''
# xxx
# '''

# x = 'a'
# y = 'b'
# print(x)
# print(y)
# print(x, y)


# 条件判断语句
# age = 26
# while True:
#     user_input = int(input('猜猜我的年纪？'))
#     if user_input < age:
#         print('小了！！！')
#     else:
#         if user_input > age:
#             print('大了！！！')
#         else:
#             print('牛！！！')
#             break
# while True:
#     user_input = int(input('猜猜我的年纪？'))
#     if user_input < age:
#         print('小了！！！')
#     elif user_input > age:
#             print('大了！！！')
#     else:
#         print('牛！！！')
#         break

# a = 10
# b = input('请输入')
# if a == b:
#     print('对')
# else:
#     print('不对')


# 常用类型：整型（int()），浮点型（float()），字符串（str()）;这些是强制类型转化的方法，但是有安全隐患
# a = 321
# b = 'nicaishi'
# c = 321.9
# d = int(b)
# print(d)
# print(type(d))

# python默认input接收的数据全部是字符串
# user_input = input('猜猜我的年纪？')
# print(user_input)
# print(type(user_input))

# 字符串是可以进行大小比较的符串
# a = 'mena'
# b = 'name'
# print(a == b)

# 给多个变量赋值
# a = b = c = 1
# print(a, b, c)
# a, b, c = 1, 2, 'jion'
# print(a, b, c)

# 常用标准数据类型
# Number（数字）：int(整型), long（长整型）, float（浮点型）, complex（复数） 
# String（字符串）：是由数字、字母、下划线组成的一串字符
# List（列表）:可以理解为可以存放任意东西（数字，字符串等）的架子，其元素是由[]存储的
# Tuple（元组）：相当于只读列表，无法对其进行改动（但是可以进行查，也可以把它作为整体进行操作，如拼接），其元素是由()储存的
# Dictionary（字典）：是升级版列表，由键值对构成，字典中的键即可以自定义的索引

# 关于切片：索引从0开始
# [m:n]表示从索引m到n之间共n-m个
# [m:]表示从索引m到末尾
# [:]表示复制
# [m:-n]表示索引m到反向索引n之间
# content = 'mynameisAguang'
# # name = content[3:-3]
# # print(name)
# single = content[8]
# print(single)

#字符串的操作
# a = 'hellohello'
# b = 'littlegirl'
# print(a + ' ' + b)

# 列表
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
# temp = list[-1]
# size = len(list) #len()函数获取列表以及字符串的长度
# print(temp)
# print(size)
# res = list + tinylist #列表的加法是列表内容的简单叠加，只能列表之间进行加法
# print(res)
# 添加元素
# list.append('aguang')
# print(list)
# 删减元素:
# a = list.pop() #pop(index)可以指定元素索引进行删除，不输入索引则默认删除最后一个元素
# print(a)
# list.remove('john') #remove(value)是指定元素进行删除
# list.clear() #清空列表
# list[3] = 'aguang' #指定元素索引进行更改
# print(list)

# 布尔bool类型：True或者False
# 列表元素的排序，默认从小到大，reverse=False
# a = [1, 4, 2, 0, 7, 3, 1, 9, 6]
# a.sort(reverse=True) 

# 字符串操作
# b = 'asdfghjkliuytre'
# c = b.upper()
# print(b)
# print(c)
# d = c.lower()
# print(d)
# e = c.split('G')
# print(e)

# a = {}
# a['aguang'] = 'shabi'
# a['jiali'] = 'fairy'
# print(a)
# a['aguang'] = 'shuaige'
# print(a)

import this