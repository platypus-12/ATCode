N = int(input())
_sum = 0
for i in range(N):
				tmp = input().split()
				if tmp[1] == "JPY":
								_sum += float(tmp[0])
				else:
								_sum += float(tmp[0]) * 380000 

print(_sum)


