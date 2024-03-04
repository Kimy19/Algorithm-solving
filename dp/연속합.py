#백준 1912
n = int(input())
num = list(map(int,input().split()))
print(num)

dp = num[:]
for i in range(1,n):
	dp[i] = max(dp[i-1]+num[i], num[i])
print(dp)


# dp = num[:]
# for i in range(2, n+1): 
# 	for j in range(n,i-1,-1):
# 		dp[j] = max(dp[j-i+1]+num[j], dp[j])

# print(max(dp[1:]))