#백준 6118
from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,input().split())
	graph[i].append(j)
	graph[j].append(i)

q = deque()
q.append(1)
visit = [0 for _ in range(n+1)]
visit[1] = 1
while q:
	cur = q.popleft()
	for i in graph[cur]:
		if visit[i]:
			continue
		visit[i] = visit[cur] + 1
		q.append(i)

count = 0
max_num = 0
ans_list = []
for i in range(1,len(visit)):
	max_num = max(max_num,visit[i]-1)

node = 1
for i in range(1,len(visit)):
	if visit[i] == max_num+1:
		node = i
		break
ans_list.append(node)
ans_list.append(max_num)
ans_list.append(visit.count(max_num+1))
print(*ans_list)
