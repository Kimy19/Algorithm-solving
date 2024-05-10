#baekjoon 1197
from collections import deque
import sys
import heapq

v,e = map(int,sys.stdin.readline().split())
included = [ 0 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for _ in range(e):
	i,j,k = map(int,sys.stdin.readline().split())
	graph[i].append((k,j))
	graph[j].append((k,i))

arr = []
for edge in graph[1]:
	heapq.heappush(arr, edge)
included[1] = 1
ans = 0
count = 0
while (count < v - 1):
	cost,node = heapq.heappop(arr)
	if included[node]:
		continue
	included[node] = 1
	ans += cost
	count += 1
	for edge in graph[node]:
		if included[edge[1]]:
			continue
		heapq.heappush(arr,edge)
print(ans)