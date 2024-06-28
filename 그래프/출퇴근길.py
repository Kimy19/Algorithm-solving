#softeer
import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
graph_rev = [[]for _ in range(n+1)]

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    graph[i].append(j)
    graph_rev[j].append(i)
s,t = map(int,sys.stdin.readline().split())

def dfs(cur,g,visit):
    if visit[cur] == 1:
        return
    visit[cur] = 1
    for i in g[cur]:
        dfs(i,g,visit)
        
visit1 = [0 for _ in range(n+1)]
visit1[t] = 1
dfs(s,graph,visit1)

visit2 = [0 for _ in range(n+1)]
visit2[s] = 1
dfs(t,graph,visit2)

visit3 = [0 for _ in range(n+1)]
dfs(s,graph_rev,visit3)

visit4 = [0 for _ in range(n+1)]
dfs(t,graph_rev,visit4)

count = 0
for i in range(1,n+1):
    if visit1[i] and visit2[i] and visit3[i] and visit4[i]:
        count+=1
print(count-2)