#baekjoon 9372
import heapq
import sys
from collections import deque

t = int(input())

ans = []
for _ in range(t):
	n,m = map(int,sys.stdin.readline().split())
	graph = [[] for _ in range(n+1)]
	for _ in range(m):
		i,j = map(int,sys.stdin.readline().split())
		graph[i].append(j)
		graph[j].append(i)
	visited = [0 for _ in range(n+1)]
	# arr = []
	arr = deque()
	for e in graph[1]:
		arr.append(e)
		# heapq.heappush(arr,e)
	visited[1] = 1
	count = 0
	while count < n-1:
		cur = arr.popleft()
		# cur = heapq.heappop(arr)
		if visited[cur]:
			continue
		visited[cur] = 1
		for e in graph[cur]:
			if visited[e]:
				continue
			arr.append(e)
			# heapq.heappush(arr,e)
		count += 1
	ans.append(count)

for i in ans:
	print(i)


