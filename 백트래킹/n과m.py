#백준 15649
n,m = map(int,input().split())
arr = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]
def dfs(cur):
	global n
	global m
	global arr
	global used
	if m == cur:
		print(*arr[:m])
		return
	for i in range(1,n+1):
		if used[i]:
			continue
		arr[cur] = i
		used[i] = 1
		dfs(cur+1)
		used[i] = 0

dfs(0)
