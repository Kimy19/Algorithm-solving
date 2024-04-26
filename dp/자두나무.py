# 2240
t,w = map(int,input().split())
list = [0]
for i in range(t):
	temp = int(input())
	list.append(temp)

dp = [[0 for _ in range(w+1)] for _ in range(t+1)]

for i in range(1, t+1):
	if list[i] == 1:
		dp[i][0] = dp[i-1][0] + 1
	else:
		dp[i][0] = dp[i-1][0]
	for j in range(1,w+1):
		if list[i] == 2 and j%2 == 1:
			dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + 1
		elif list[i] == 1 and j%2 == 0:
			dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + 1
		else:
			dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])
print(max(dp[t]))
			
	