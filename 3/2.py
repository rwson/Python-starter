#coding=utf-8

'''
	切片和字符串常见操作
'''

import random

name = "abcdefg"

#	从start到end - 1
print(name[0:4])

#	从start到(字符串总长度 - end)
print(name[0:-4])

#	从start到最后
print(name[0:])

#	len方法获取长度

name2 = "x" * random.randint(200, 1000)
print(len(name2))

#	步长为10
print(name2[::10])

name3 = "xaskdjnasdnjaksdnkajsndkjasndkjansdkjasnjdkasjdnaksdhaisdh"

#	从后取字符串, 字符串逆序
print(name3[::-1])

#	从后往前取, 第abs(start)个字符
print(name3[-1])

print("-" * 30)
