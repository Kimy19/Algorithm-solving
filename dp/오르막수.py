#baekjoon
n = int(input())

# dp = [[0 for _ in range(n+1)] for _ in range(10)]
# for i in range(1,n+1):
# 	dp[0][i] = 1
# for i in range(10):
# 	dp[i][0] = i+1

# for i in range(10):
# 	for j in range(1,n+1):
# 		dp[i][j] = (dp[i][j-1] + dp[i-1][j])%10007
# print(dp[9][n-1])


dp = [1 for _ in range(10)]
for i in range(n-1):
	for j in range(1,10):
		dp[j] += dp[j-1]
print(sum(dp)%10007)
