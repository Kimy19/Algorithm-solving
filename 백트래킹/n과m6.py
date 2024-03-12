#백준 15650
n, m = map(int,input().split())
num = list(map(int,input().split()))
num = sorted(num)
visit = [0 for _ in range(10000)]
arr = [0 for _ in range(m+1)]
def func(cur):
	global m
	global used
	global arr
	if cur == m+1:
		print(*arr[1:])
		return

	for i in num:
		if i<=arr[cur-1]:
			continue
		if visit[i]:
			continue
		arr[cur] = i
		visit[i] = 1
		func(cur+1)
		visit[i] = 0

func(1)
