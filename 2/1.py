#coding=utf-8

'''
	与或非
	and or not
'''

username = input("请输入用户名: ")
password = input("请输入密码: ")

if (username == "rwson" and password == "123456") or (username == "srw" and password == "123"):
	print("登录成功!")
else:
	print("登录失败")

print("-" * 30)

wifiGoBank = input("老婆大人, 您去银行吗? [1: 去, 2: 不去]")
isFree = input("自己有空去银行吗? [1: 去, 2: 不去]")

if wifiGoBank == "1" and isFree == "1":
	print("可以办业务")
else:
	print("两人必须同时到场!")

