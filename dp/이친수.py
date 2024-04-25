# 백준 2193

n = int(input())
dp0 = [0 for _ in range(n+1)]
dp1 = [0 for _ in range(n+1)]

dp0[1] = 0
dp1[1] = 1

for i in range(2,n+1):
	dp0[i] = dp1[i-1] + dp0[i-1] 
	dp1[i] = dp0[i-1]

print(dp0[n] + dp1[n])