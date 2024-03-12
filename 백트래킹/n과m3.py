#백준 15650
n, m = map(int,input().split())

arr = [0 for _ in range(m)]
def func(cur):
	global m
	global used
	global arr
	if cur == m:
		print(*arr[:])
		return

	for i in range(1,n+1):
		arr[cur] = i
		func(cur+1)

func(0)
