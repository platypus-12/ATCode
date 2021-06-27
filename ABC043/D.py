import sys

# print(11111 < float("inf"))

s = input()

length = len(s)
tmp_char = ''
same_flg = False
start_num = []


for i, x in enumerate(s):
	if i == 0:
		tmp_char = x
	elif tmp_char == x:
		same_flg = True
		start_num.append(i)
	elif same_flg == True and tmp_char != x:
		print(min(start_num) - 1, i)
		sys.exit()
	else:
		tmp_char = x

print(-1, -1)


