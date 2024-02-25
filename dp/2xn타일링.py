#[백준 11726  2×n 타일링] https://www.acmicpc.net/problem/11726
dp = [0]*1001

n = int(input())
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
	dp[i] = dp[i-1]+dp[i-2]

print(dp[n]%10007)