#coding=utf-8

'''
	判断语句

	if 条件:
		条件成立
	else:
		条件不成立
'''

age = 18

if age >= 18:
	print("你已经年满18周岁, 可以上网!")
else:
	print("你未年满18周岁, 不可以上网!")

print("-" * 30)

current = int(input("请输入当前的分数: "))

types = int(input("请输入你违反交通规则序号(1. 闯红灯, 2. 违章停车): "))

if types == 1:
	current -= 6
else:
	current -= 3

print("当前剩余分数: %d"%current)
