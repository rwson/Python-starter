#coding=utf-8 

'''
	while循环
	while True
		//	...
'''

import random

while True:
	player = int(input("请选择[0: 剪刀, 1: 石头, 2: 布]"))

	computer = random.randint(0, 2)

	if (computer == 2 and player == 0) or (computer == 0 and player == 1) or (computer == 1 and player == 2): 
		print("你赢了, 好棒哦!")
	elif computer != player:
		print("你输了, 继续努力!")
	else:
		print("平局!")
