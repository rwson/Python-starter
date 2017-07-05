#coding=utf-8

num = int(input("请输入一个数字: "))

if not (num >= 4 and num <= 10):
	print("中奖啦!")
else:
	print("你没中奖!")

scroe = int(input("你考了多少分? "))

if (scroe >= 90):
	print("哇!太棒了!")
elif (scroe < 90 and scroe >= 80):
	print("还不错, 挺好的!")
elif (scroe < 80 and scroe >= 60):
	print("下次继续努力!")
else:
	print("回去要挨打了!")
