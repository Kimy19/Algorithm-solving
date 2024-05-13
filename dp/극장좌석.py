#baekjoon 2302

n = int(input())
k = int(input())
vip = [0 for _ in range(n+1)]
for _ in range(k):
	i = int(input())
	vip[i] = 1

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
	if vip[i] or vip[i-1]:
		dp[i] = dp[i-1]
	else:
		dp[i] = dp[i-2] + dp[i-1]
print(dp[n])