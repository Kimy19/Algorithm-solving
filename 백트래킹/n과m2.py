#백준 15650
n, m = map(int,input().split())

used = [0 for _ in range(n+1)]
arr = [0 for _ in range(m+1)]
def func(cur):
	global m
	global used
	global arr
	if cur == m+1:
		print(*arr[1:])
		return

	for i in range(arr[cur-1]+1,n+1):
		if used[i]:
			continue
		arr[cur] = i
		used[i] = 1
		func(cur+1)
		used[i] = 0

func(1)
