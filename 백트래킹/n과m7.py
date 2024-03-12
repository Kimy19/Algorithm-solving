#백준 15650
n, m = map(int,input().split())
num = list(map(int,input().split()))
num = sorted(num)
arr = [0 for _ in range(m)]
def func(cur):
	global m
	global used
	global arr
	if cur == m:
		print(*arr[:])
		return

	for i in num:
		arr[cur] = i
		func(cur+1)

func(0)
