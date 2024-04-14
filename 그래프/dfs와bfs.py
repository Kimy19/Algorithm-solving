#백준 1260
from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
for i in range(n+1):
    graph[i] = sorted(graph[i])

#bfs
q = deque()
visit = [0 for _ in range(n+1)]
bfs_ans = []
q.append(v)
visit[v] = 1
bfs_ans.append(v)
while q:
    cur = q.popleft()
    for i in graph[cur]:
        if visit[i]:
            continue
        visit[i] = 1
        q.append(i)
        bfs_ans.append(i)

#dfs
visit = [0 for _ in range(n+1)]
dfs_ans =[]
def dfs(i):
    global visit,graph,dfs_ans

    if visit[i]:
        return
    visit[i] = 1
    for j in graph[i]:
        if visit[j]:
            continue
        dfs_ans.append(j)
        dfs(j)

dfs_ans.append(v)
dfs(v)

print(*dfs_ans)
print(*bfs_ans)