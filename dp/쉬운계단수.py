n= int(input())

dp1 = [0,1,1,1,1,1,1,1,1,1]
dp2 = [0 for i in range(10)]

ans = sum(dp1)
for i in range(2,n+1):
	if i%2 == 0:
		for j in range(10):
			if j-1>=0:
				dp2[j-1] += dp1[j]
			if j+1<=9:
				dp2[j+1] += dp1[j]
		ans = sum(dp2)
		dp1 = [0 for i in range(10)]
		
	
	else:
		for j in range(10):
			if j-1>=0:
				dp1[j-1] += dp2[j]
			if j+1<=9:
				dp1[j+1] += dp2[j]
		dp2 = [0 for i in range(10)]
		ans = sum(dp1)

print(ans%1000000000)