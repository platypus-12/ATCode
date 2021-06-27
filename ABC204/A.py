# x = int(input())
# s = input()
# # # 整数が複数書かれた行
# x, y, z = map(int, input().split())
# # xyz = list(map(int, input().split()))
# # xyz = [int(t) - 1 for t in input().split()]


# # 整数が複数書かれた複数行
# from sys import stdin
# for _ in range(n):
#   x, y, z = map(int, stdin.readline().split())

# # 別の方法
# xyzs = [list(map(int, stdin.readline().split())) for _ in range(n)]


# 文字列が書かれた複数行
# 文字列の場合には改行が残ることが問題になるので、[:-1] スライスで改行を除去する.
# from sys import stdin
# for _ in range(n):
#   # stdin.readline().rstrip('\n') より速い
#   s = stdin.readline()[:-1]

# 別の方法
# ss = [stdin.readline()[:-1] for _ in range(n)]

# INF = 10 ** 18

# from functools import lru_cache

# @lru_cache(maxsize=None)
# def dfs(x):

_list = [0,1,2]
x, y = map(int, input().split())


if x == y:
	print(x)
else:
	_list.remove(x)
	_list.remove(y)
	print(_list[0])

