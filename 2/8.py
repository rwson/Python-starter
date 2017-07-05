#coding=utf-8 

'''
	continue, break
'''

i = 0
while i < 10:
	i += 1
	print(i)
	if i == 5:
		break

print("-" * 30)

i = 0
while i < 10:
	i += 1
	print(i)
	if i == 5:
		print("-" * 10)
		continue