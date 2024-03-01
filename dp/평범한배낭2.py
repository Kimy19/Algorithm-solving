# #n:물건개수 m:최대무게
# n, m = map(int,input().split())
# v =[0] #무게
# c = [0] #가치
# k =[0] #개수
# for i in range(n):
# 	t1,t2,t3 = map(int,input().split())
# 	v.append(t1)
# 	c.append(t2)
# 	k.append(t3)
# dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(2)]
# for i in range(m+1): # i == current_weight
# 	for j in range(n+1): # j == number of object
# 		if(v[j] <= i):
# 			print(i,j)
# 			# print(dp[i-v[j]][j][1])
# 			if dp[1][i-v[j]][j] < k[j]: #같은 물건의 개수 확인
# 				dp[0][i][j] = max(dp[0][i][j-1],dp[0][i-v[j]][j] + c[j])
# 				dp[1][i][j] = dp[1][i-v[j]][j] +1 #사용한 개수 저장

# 			else:
# 				dp[0][i][j] = max(dp[0][i][j-1],dp[0][i-v[j]][j-1] + c[j])
# 				dp[1][i][j] = 1
# 		else:
# 			dp[0][i][j] = dp[0][i][j-1]

# print(dp[0][m][n])



#n:물건개수 m:최대무게
n, m = map(int,input().split())
v =[0] #무게
c = [0] #가치
for i in range(n):
	t1,t2,t3 = map(int,input().split())
	temp = 1

	while t3>0:
		num = min(temp,t3)
		v.append(t1*num)
		c.append(t2*num)
		t3 -= temp
		temp *= 2

dp = [0 for _ in range(m+1)]

for i in range(len(v)):
	for j in range(m,v[i]-1,-1):
		if v[i] <= j:
			dp[j] = max(dp[j],dp[j-v[i]] + c[i])

print(dp[m])