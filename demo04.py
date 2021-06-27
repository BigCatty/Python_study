from math import pi
import random

# A = []
# for _ in range(100):
#     a = random.random() * 3 + 3.5
#     A.append(a)

# print(A)
# print(min(A), max(A))

# 问题：real_age = randint(18, 30)，写一个程序，用户猜age，猜对退出，猜错继续猜
# From Jiali Zhang

# version 1.0
# age = int(input('猜猜我的年龄：'))
# real_age = random.randint(18,30)
# while age != real_age:
#     if age < real_age:
#         print('小了！')
#         age = int(input('猜猜我的年龄：'))
#     else:
#         print('大了！')
#         age = int(input('猜猜我的年龄：'))
# else:
#     print('猜对了！')

# version 2.0
# real_age = random.randint(18,30)
# while True:
#     age = int(input('猜猜我的年龄：'))
#     if age < real_age:
#         print('小了！')
#     elif age > real_age:
#         print('大了！')
#     else:
#         print('猜对了！')
#         break

# version 3.0
# 用户只有三次机会，猜不对就骂他是傻逼
# real_age = random.randint(18,30)
# for i in range(5):
#     age = input('猜猜我的年龄：')
    
    # 用户输入检测
    # while True:
    #     try:
    #         age = int(age)
    #         break
    #     except:
    #         age = input('输错了，重新输入：')

    # if age < real_age:
    #     print('小了！')
    # elif age > real_age:
    #     print('大了！')
    # else:
    #     print('你真聪明！')
    #     break

    # if i != 4:
    #     print('还剩' + str(4-i) + '次')
    # else:
    #     print('你是傻逼吧！')
