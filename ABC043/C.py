N = int(input())
# 整数が複数書かれた行

xyz = list(map(int, input().split()))

# _min = min(xyz)
# _max = max(xyz)

min_sum = 1000000

for x in range(-110, 110):
	sum_cost = 0
	for y in xyz:
		cost = (x-y) ** 2
		sum_cost += cost
	# print(sum_cost, "sum_cost")
	min_sum = min(min_sum, sum_cost)

print(min_sum)
		


