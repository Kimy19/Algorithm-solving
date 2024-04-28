# 백준 2660
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
while (1):
	i,j = map(int,input().split())
	if i == -1:
		break
	graph[i].append(j)
	graph[j].append(i)

q = deque()
ans = 0
ans_list = []
for i in range(1,n+1):
	visit = [0 for _ in range(n+1)]
	q.append(i)
	visit[i] = 1
	ans = 0
	while q:
		cur = q.popleft()
		for j in graph[cur]:
			if visit[j]:
				continue
			q.append(j)
			visit[j] = visit[cur] + 1
			ans = max(ans,visit[j] - 1)
	ans_list.append((i,ans))
		
min_value = min(x[1] for x in ans_list)
sorted_list = sorted((x for x in ans_list if x[1] == min_value), key = lambda x : x[0])
print(min_value, len(sorted_list))
temp = []
for i in sorted_list:
	temp.append(i[0])
print(*temp)
