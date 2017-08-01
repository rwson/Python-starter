#coding=utf-8

'''
	字符串常见操作
'''
aStr = "hello Python,my name is srw"

#	find、rfind: 类似于indexOf、lastIndexFf
print(aStr.find("srw"))

print("-" * 30)

print(aStr.find("src"))

print("-" * 30)

#	index、rindex: 类似find、 rindex, 但是找不到会抛出异常
print(aStr.index("srw"))

print("-" * 30)

print(aStr.rindex("srw"))

print("-" * 30)

#	抛出(ValueError: substring not found)
#	print(aStr.index("src"))
#	print(aStr.rindex("src"))

#	count: 获取出现的次数
print(aStr.count("e"))

print("-" * 30)

#	count(str, start, end)
print(aStr.count("e", 10, 12))

print("-" * 30)

#	replace: 替换字符串
print(aStr.replace(" ", "-"))

print("-" * 30)

#	replace(old, new, cound): 替换字符串多少次
print(aStr.replace(" ", "-", 1))

print("-" * 30)

#	split: 按照某个分隔符拆分
print(aStr.split(" "))

#	split(str, maxsplit): 按照某个分隔符拆分
print(aStr.split(" ", 2))

print("-" * 30)

#	capitalize: 字符串首字母大写
print(aStr.capitalize())

print("-" * 30)

#	capitalize: 每个单词首字母大写
print(aStr.title())

print("-" * 30)

#	startswith: 是否为某个字符串开始
print(aStr.startswith("H"))

print("-" * 30)

print(aStr.startswith("h"))

print("-" * 30)

#	startswith: 是否为某个字符串结尾
print(aStr.endswith("W"))

print("-" * 30)

print(aStr.endswith("w"))

print("-" * 30)

#	lower: 转成小写
print(aStr.title().lower())

print("-" * 30)

#	lower: 转成大写
print(aStr.title().upper())
