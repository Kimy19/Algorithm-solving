#baekjoon15988

t = int(input())
num = []
for _ in range(t):
	n = int(input())
	num.append(n)
n = max(num)
dp = [0,1,2,4]
for i in range(4,n+1):
	dp.append((dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009)

for i in num:
	print(dp[i])