#coding=utf-8

'''
	格式化输出
	%(xxx, yyy)取出多个变量的值

	常用的格式符:
	%c 	字符的ASC码
	%s 	通过str()字符串换来格式化
	%i  有符号的十进制数
	%u  无符号的十进制数
	%o  八进制整数
	%x  十六进制整数(小写)
	%X  十六进制整数(大写)
	%e  索引符号(小'e')
	%E  索引符号(大'E')
	%f  浮点实数
	%g  %f和%e的简写
	%G  %F和%E的简写
'''

name = "rwson"
age = 24

print("name is %s"%name)
print("---------------")
print("my name is %s,and age is %d"%(name, age))

print("---------------")

print("aaaaaaaa", end = " - ")
print("bbbbbbbb")
