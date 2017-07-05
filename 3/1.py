#coding=utf-8

'''
	for循环(类似js中的for...in枚举)
'''

name = input("请输入你的姓名: ")

for item in name:
	print(item)

for tmp in range(0, 10):
	print("当前为: %d"%tmp)
