n = int(input())
xor_n = 0
for i in range(1, n+1):
	xor_n = xor_n ^ i
input_nums = [int(i) for i in input().split()]
for num in input_nums:
	xor_n = xor_n ^ num
print(xor_n)