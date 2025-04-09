n = int(input())
if (n == 1):
	print(n)
elif (n <= 3):
	print("NO SOLUTION")
else:
	odd = list(range(1, n+1, 2))
	even = list(range(2, n+1, 2))
	print(" ".join(str(i) for i in (even+odd)))