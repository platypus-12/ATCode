S = input()

a = S.split("/")

import datetime

b = datetime.datetime(int(a[0]),int(a[1]),int(a[2]))

k = datetime.datetime(int("2019"), int("04"), int("30"))

if k >= b:
				print("Heisei")
else:
				print("TBD")
