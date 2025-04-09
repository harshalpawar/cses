seq = input()
curr = ''
count = 0
sol = 0
for c in seq:
	if c != curr:
		sol = max(sol, count)
		curr = c
		count = 1
	else:
		count += 1
sol = max(sol, count)
print(sol)
