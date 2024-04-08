#백준 11286
import sys
import heapq
#heap.heappush(h,(a,b))일때 a,b순으로 비교하여 힙구성
h = []
n = int(input())
ans = []
for _ in range(n):
	num = int(sys.stdin.readline())
	if num != 0:
		heapq.heappush(h,(abs(num),num))
	else:
		if h:
			ans.append(heapq.heappop(h)[1])
		else:
			ans.append(0)

for i in ans:
	print(i)