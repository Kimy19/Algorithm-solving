#baekjoon 1167
import sys
from collections import deque

v = int(input())
graph = [[] for _ in range(v+1)]
graph2 = [[] for _ in range(v+1)]
for i in range(1,v+1):
	row = list(map(int,sys.stdin.readline().split()))
	index = row[0]
	for j in range(1,len(row)-1,2):
		graph[index].append([row[j], row[j+1]])
		graph2[index].append([row[j], row[j+1]])

q = deque()
#node, cost, parent
q.append([1, 0, 1])
dist = [ -1 for _ in range(v+1)]
dist[1] = 0
while q:
	node, cost , parent = q.popleft()
	dist[node] = dist[parent] + cost
	for i in graph[node]:
		if dist[i[0]] == -1:
			i.append(node)
			q.append(i)
max_index = dist.index(max(dist))

q = deque()
q.append([max_index, 0, max_index])
dist = [-1 for _ in range(v+1)]
dist[max_index] = 0
while q:
	node, cost, parent = q.popleft()
	dist[node] = dist[parent] + cost
	for i in graph2[node]:
		if dist[i[0]] == -1:
			i.append(node)
			q.append(i)

print(max(dist))
