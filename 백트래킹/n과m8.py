#백준 15650
n, m = map(int,input().split())
num = list(map(int,input().split()))
num = sorted(num)
arr = [1 for _ in range(m+1)]
def func(cur):
	global m
	global used
	global arr
	if cur == m+1:
		print(*arr[1:])
		return

	for i in num:
		if arr[cur-1] > i:
			continue
		arr[cur] = i
		func(cur+1)

func(1)
