n, k = map(int,input().split())
v = [0]
w = [0]
for i in range(n):
	t1,t2 = map(int,input().split())
	w.append(t1)
	v.append(t2)
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(k+1): # i == current_weight
	for j in range(n+1): # j == number of object
		if(w[j] <= i):
			dp[i][j] = max(dp[i][j-1],dp[i-w[j]][j-1] + v[j])
		else:
			dp[i][j] = dp[i][j-1]

print(dp[k][n])

# #배열 하나 사용
# n, k = map(int,input().split())
# v = [0]
# w = [0]
# for i in range(n):
# 	t1,t2 = map(int,input().split())
# 	w.append(t1)
# 	v.append(t2)

# dp = [0 for i in range(k+1)]
# for i in range(1,n+1): #물건
# 	for j in range(k,0,-1):# 무게
# 		if w[i] <= j:
# 			dp[j] = max(dp[j],dp[j-w[i]] + v[i])
# print(dp)



	