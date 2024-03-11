n = int(input())
visit = [0 for _ in range(n)]

visit1 =[0 for _ in range(n*2-1)]
visit2 =[0 for _ in range(n*2-1)]

def dfs(cur):
	global queen
	global n
	count = 0
	if cur == n:
		return 1
	for i in range(n):#가능한 위치
		if visit[i] or visit1[cur+i] or visit2[cur-i+n-1]:
			continue
		visit[i] = 1
		visit1[cur+i] = 1
		visit2[cur-i+n-1] = 1
		count+=dfs(cur+1)
		visit[i] = 0
		visit1[cur+i] = 0
		visit2[cur-i+n-1] = 0
	return count

print(dfs(0))