#baekjoon 22856
import sys

sys.setrecursionlimit(1000000)
n = int(input())
lc = [-1 for _ in range(n+1)]
rc = [-1 for _ in range(n+1)]

for _ in range(n):
	a,b,c = map(int,sys.stdin.readline().split())
	if b!= -1:
		lc[a] = b
	if c!= -1:
		rc[a] = c

visit = [0 for _ in range(n+1)]

path = []
count = 0
step = 0
def tree_search(cur):
	global path,count,step,visit,lc,rc
	if cur == -1 or visit[cur]:
		return
	step += 1
	print(cur)
	if lc[cur] == -1:
		if rc[cur] == -1:
			visit[cur] = 1
			path.append(cur)
			count += 1
			if count == n:
				print(step-1)
				exit(0)
			return
	if lc[cur] != -1:
		tree_search(lc[cur])
		step += 1
		print(cur)
	visit[cur] = 1
	path.append(cur)
	count += 1
	if count == n:
		print(step-1)
		exit(0)
	if rc[cur] != -1:
		tree_search(rc[cur])
		step += 1
		print(cur)

tree_search(1)
