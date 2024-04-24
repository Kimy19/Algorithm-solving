#백준 4803
import sys
from collections import deque

num = 0
ans_list = []
while 1:
	num += 1
	n, m = map(int,input().split())
	if n == 0:
		break
	graph = [[] for _ in range(n+1)]
	for _ in range(m):
		i,j = map(int,input().split())
		graph[i].append(j)
		graph[j].append(i)
	count = 0
	checked = [0 for _ in range(n+1)]
	for root in range(1,n+1):
		if checked[root]:
			continue
		visit = [0 for _ in range(n+1)]
		p = [0 for _ in range(n+1)]
		q = deque()
		q.append(root)
		visit[root] = 1
		flag = 0
		while q:
			cur = q.popleft()
			for nxt in graph[cur]:
				if nxt == p[cur]:
					continue
				if visit[nxt]:
					flag = 1
					break
				visit[nxt] = 1
				p[nxt] = cur
				q.append(nxt)
			if flag:
				break
		if flag == 0:
			count += 1
			for k in range(1,n+1):
				if visit[k]:
					checked[k] = visit[k]
	if count == 0:
		ans_list.append("Case %d: No trees." % (num))
	elif count == 1:
		ans_list.append("Case %d: There is one tree." % (num))
	elif count > 1:
		ans_list.append("Case %d: A forest of %d trees." % (num,count))

for i in ans_list:
	print(i)
