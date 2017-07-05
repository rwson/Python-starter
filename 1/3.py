#coding=utf-8

name = input("input your name:")
age = input("input your age:")
job = input("input your job:")

print("-------------")
'''
	input中获取的值为字符串(在python2中用raw_input方法接受输入的值, python2中的input会当成一个表达式执行)
	所以某些特殊格式需要转换,比如数字用int方法
'''
print("your name is %s, your age is %d, your job is %s"%(name, int(age), job))