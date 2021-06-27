# x = int(input())
s = input()

result = ''
for x in s:
	if x == '0':
		result += '0'
	elif x == '1':
		result += '1'
	else:
	    result = result[:-1]


print(result)