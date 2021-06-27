N,A,B,C = map(int, input().split())

data = [int(input()) for _ in range(N)]

print(data)


_list = [3]
print(type(_list))
_list[0] = []
_list[1] = []
_list[2] = []

for i, x in enumerate(data):
				_list[0].append(x - A)
				_list[1].append(x - B)
				_list[2].append(x - C)

				print(abs(x - A))
				print(abs(x - B))
				print(abs(x - C))


