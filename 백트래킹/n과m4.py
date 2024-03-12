#백준 15650
n, m = map(int,input().split())

arr = [1 for _ in range(m+1)]
def func(cur):
	global m
	global used
	global arr
	if cur == m+1:
		print(*arr[1:])
		return

	for i in range(arr[cur-1],n+1):
		arr[cur] = i
		func(cur+1)

func(1)
