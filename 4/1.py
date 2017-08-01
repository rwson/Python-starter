#coding=utf-8

'''
	列表

	列表中元素可以为任意类型的多个数据
'''

names = ["rwson", "sonrw", "srw"]

print(type(names))

infos = ["rwson", 25, 92.7]

print(infos[0])

#	for x in val: 遍历多种值
for tmp in infos:
	print(tmp)

print("-" * 30)

#	while循环
i = 0
length = len(infos)

while i < length:
	print(infos[i])
	i += 1


namesList = ["sonrw", "test", "fuck"]
name = input("input your name:")

while name.strip() == "":
	name = input("input your name:")

flag = ""
for nameC in namesList:
	if nameC == name:
		flag = name
		break


if len(flag) == 0:
	print("not found!")
else:
	print("target name is %s"%flag)