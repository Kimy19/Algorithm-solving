#백준 13398

n = int(input())
num = list(map(int,input().split()))

dp = [[0 for i in range(n)] for j in range(2)]
dp[0] = num[:]
print(dp)

for i in range(1, n):
	dp[0][i] = max(dp[0][i-1]+num[i], num[i])
	dp[1][i] = max(dp[0][i-1], dp[1][i-1] + num[i])

print(max(max(dp[0]),max(dp[1])))
