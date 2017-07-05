#coding=utf-8

'''
	运算符

	基础运算符:
	+, -, *, /, //(取整数), %(取余数), **(取幂)

	复合赋值运算符
	+=, -=, *=, /=, //=, %=, **=
'''

a = 11
b = 2

#  python2中输出5
print(a/b)

print("------------")

a = 11.0
b = 2

print(a/b)

print("------------")

a = 11.0
b = 2.0

print(a//b)

print("------------")

print(2**100)

print("-"*30)

c, d = 1, 2

print(c, d)

print("-"*30)

#  交换c, d的值
c, d = d, c

print(c, d)

print("-"*30)

c += 1
d += 1
d **= 10

print(c, d)

print("-"*30)

c *= 1 + 2 + 300
print(c)
