#백준 15650
import copy 

n, m = map(int,input().split())
num = list(map(int,input().split()))
num = sorted(num)
arr = [0 for _ in range(m)]
visit = [0 for _ in range(n+1)]
def func(cur):
	global m
	global used
	global arr
	if cur == m:
		print(*arr[:])
		return

	prev = -1
	for index,i in enumerate(num):
		
		if prev== i or visit[index]:
			continue
		prev = i
		arr[cur] = i
		visit[index] = 1
		func(cur+1)
		visit[index] = 0

func(0)