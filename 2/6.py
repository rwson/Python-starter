#coding=utf-8 

i = 1

res = 0
total = 0

while (i <= 100 and i >= 1):
	if (i % 2 == 0):
		print("当前数字为: %d"%i)
		res += i
	i += 1
	total += i

print("1~100之间所有偶数和为: %d"%res)
print("1~100之间所有数和为: %d"%total)

print("-" * 30)

start = 1
while (start <= 5):
	j = 1
	while (j <= start):
		print("*", end = " ")
		j += 1

	print()
	start += 1

while (start >= 1):
	j = 1
	while (j <= start):
		print("*", end = " ")
		j += 1

	print()
	start -= 1

print("-" * 30)
