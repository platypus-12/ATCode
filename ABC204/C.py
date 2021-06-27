# x = int(input())
# s = input()
# # 整数が複数書かれた行
# x, y, z = map(int, input().split())
# xyz = list(map(int, input().split()))
# xyz = [int(t) - 1 for t in input().split()]


# # 整数が複数書かれた複数行
# from sys import stdin
# for _ in range(n):
#   x, y, z = map(int, stdin.readline().split())

# # 別の方法
# xyzs = [list(map(int, stdin.readline().split())) for _ in range(n)]


# # 文字列が書かれた複数行
# # 文字列の場合には改行が残ることが問題になるので、[:-1] スライスで改行を除去する.
from sys import stdin
# for _ in range(n):
#   # stdin.readline().rstrip('\n') より速い
#   s = stdin.readline()[:-1]

# # 別の方法
# ss = [stdin.readline()[:-1] for _ in range(n)]

# INF = 10 ** 18

# from functools import lru_cache

# # @lru_cache(maxsize=None)
# # def dfs(x):

N, M = map(int, input().split())
# xyzs = [list(map(int, stdin.readline().split())) for _ in range(M)]
xyzs = set(stdin.readline()[:-1].replace(' ','') for _ in range(M))

# print(xyzs)

# xyzs_s = sorted(xyzs, key=lambda x: x[1])
# print(xyzs_s)

import copy
# deep_x = set()


from functools import lru_cache

# @lru_cache(maxsize=None)
def set_add(xyzs, _len):
	# _len = len(xyzs)
	# print(_len, "len")
	# global deep_x
	deep_x = copy.deepcopy(xyzs)
	for x in xyzs:
		for y in xyzs:
			print(x, y, "xy")
			if x[1] == y[0]:
				deep_x.add(x[0]+y[1])
				print(deep_x, "deep")
				if _len != len(deep_x):
					set_add(deep_x, len(deep_x))
	return deep_x


deep_x = set_add(xyzs, len(xyzs))
for x in range(1, N + 1):
	deep_x.add(str(x)+str(x))



print(deep_x)
print(len(deep_x))

