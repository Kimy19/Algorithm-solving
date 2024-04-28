# 11055

n = int(input())

num = list(map(int,input().split()))

dp = [0 for _ in range(n)]
for i in range(n):
	temp = i-1
	max_n = 0
	while temp>=0:
		if num[temp] < num[i]:
			max_n = max(max_n,dp[temp])
		temp -= 1
	dp[i] = max_n + num[i]
print(max(dp))