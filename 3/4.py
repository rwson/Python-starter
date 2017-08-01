#coding=utf-8

'''
	字符串常见操作
'''
aStr = "hello Python, my name is srw"

#	center/ljust/rjust: 中/左/右对齐显示
print(aStr.center(100))

#	lstrip/rstrip: 去除左/右空白字符
lStr = "     hello Python"

print(lStr.lstrip())

rStr = "hello Python     "

print(rStr.rstrip() + ", my name is srw")

#	strip: 去除左右空白字符
sStr = "     hello Python     "

print(sStr.strip() + ", my name is srw")

#	partition: 按照参数分隔, 并且包含原字符串

print(aStr.partition("my name"))

#	rpartition: 按照参数分隔, 并且包含原字符串(从右开始切割)
mStr = "hello Python, my name is srw, the language's name is Python"
print(mStr.rpartition("name"))

#	splitlines: 按照换行符切割
nStr = "hello Python, \nmy name is srw"
print(nStr.splitlines())

#	isalpha: 判断是否都是纯字母
iStr = "hello python， fuck"

print(iStr.isalpha())

#	isdigit: 判断是否都是纯数字
dStr = "12345678"

print(dStr.isdigit())

#	join: 字符串连接
joiner = " "

strs = ["my", "name", "is", "srw"]

print(joiner.join(strs))
