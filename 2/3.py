#coding=utf-8

# 0:没车票, 1:有车票
ticket = 1

# 刀子长度(超过20无法携带)
length = 20

if ticket == 1:
	print("有车票, 下一步安检")

	if length <= 20:
		print("安检通过")
	else:
		print("安检不通过")

else:
	print("没车票")
