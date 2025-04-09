n = int(input())
nums = [int(i) for i in input().split()]

sol = 0
last = nums[0]
for i in range(1, n):
	diff = nums[i] - last
	if diff < 0:
		last = nums[i] + abs(diff)
		sol += abs(diff)
	else:
		last = nums[i]
print(sol)