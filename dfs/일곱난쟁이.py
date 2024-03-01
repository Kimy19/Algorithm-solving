num = []
for i in range(9):
	num.append(int(input()))

choice = []
def dfs(depth, n):
	if depth == 7:
		if sum(choice) == 100:
			print('\n'.join(map(str,sorted(choice))))
			exit()
		else:
			return
	
	for i in range(n,9):
		choice.append(num[i])
		dfs(depth+1, n+1)
		choice.pop()

dfs(0,0)