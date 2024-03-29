#백준 2156
n = int(input())

wine = [0]
for i in range(n):
	wine.append(int(input()))

dp1 = [0 for _ in range(n+1)]
dp2 = [0 for _ in range(n+1)]
dp1[1] = wine[1]
dp2[1] = wine[1]
for i in range(2,n+1):
	dp1[i] = max(dp2[i-1]+wine[i],dp1[i-1])
	dp2[i] = max(dp2[i-2],dp1[i-2])+wine[i]

print(max(dp1[n],dp2[n]))