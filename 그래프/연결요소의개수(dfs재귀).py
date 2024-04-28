#백준 11724
import sys
print(sys.getrecursionlimit())
#파이썬은 재귀의 깊이가 깊어지면 에러 발생 
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
	i,j = map(int,sys.stdin.readline().split())
	graph[i].append(j)
	graph[j].append(i)

visit = [0 for _ in range(n+1)]
def dfs(i):
	global graph,visit

	visit[i] = 1
	for j in graph[i]:
		if visit[j]:
			continue
		dfs(j)

ans = 0
for i in range(1,n+1):
	if visit[i]:
		continue
	dfs(i)
	ans+=1

print(ans)