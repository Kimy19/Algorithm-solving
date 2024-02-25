
dp = [[0,0,0],[0,0,0]]
mindp = [[0,0,0],[0,0,0]]
n = int(input())

for i in range(0,n):
	row = list(map(int, input().split()))
	if i == 0:
		dp[0] = row
		mindp[0] = row
		continue
	for j in range(3):
		if j == 0:
			dp[1][j] = max(dp[0][0],dp[0][1]) + row[j]
			mindp[1][j] = min(mindp[0][0],mindp[0][1]) + row[j]
		elif j == 1:
			dp[1][j] = max(dp[0]) + row[j]
			mindp[1][j] = min(mindp[0]) + row[j]
		else:
			dp[1][j] = max(dp[0][1],dp[0][2]) + row[j]
			mindp[1][j] = min(mindp[0][1],mindp[0][2]) + row[j]

	# print(dp[1])
	dp[0] = dp[1][:]
	mindp[0] = mindp[1][:]
	
# print(dp[1],mindp[1])
if n == 1:
	print(max(dp[0]),min(mindp[0]))
else:
	print(max(dp[1]),min(mindp[1]))


