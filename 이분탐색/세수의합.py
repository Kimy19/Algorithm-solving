#백준 2295
from bisect import bisect_left,bisect_right

n = int(input())
num = [int(input()) for _ in range(n)]
num = sorted(num)


# #N^3 * logN (시간초과)
# for i in range(n-2,-1,-1):
# 	for j in range(i-1,-1,-1):
# 		for k in range(j-1,-1,-1):
# 			sum = num[i] + num[j] + num[k]
# 			if bisect_right(num,sum) - bisect_left(num,sum) > 0:
# 				print(sum)
# 				exit()

two = []
#N^2 + N^2*logN
for i in range(n):
	for j in range(i,n):
		two.append(num[i]+num[j])
two = sorted(two)

for i in range(n-1,-1,-1):
	for j in range(i,-1,-1):
		sum = num[i] - num[j]
		if bisect_right(two,sum) - bisect_left(two,sum) > 0:
			print(num[i])
			exit()
