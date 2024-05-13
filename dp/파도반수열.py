#baekjoon 9461

t = int(input())
ans = []
for _ in range(t):
	n = int(input())
	dp = [0,1,1,1,2,2]
	for i in range(6,n+1):
		dp.append(dp[i-1] + dp[i-5])
	ans.append(dp[n])

for i in ans:
	print(i)