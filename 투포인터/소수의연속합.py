#백준 1644
import math
n = int(input())

if n == 1:
	print(0)
	exit()

#에라토스테네스의 체
num = []
prime = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
	if prime[i] == True:
		j = 2
		while j * i <= n:
			prime[j*i] = False
			j+=1
for i in range(2,n+1):
	if prime[i]:
		num.append(i)
# print(num)

	

#누적합
sum = [0]
sum.append(num[0])
for i in range(1,len(num)):
	sum.append(sum[-1]+ num[i])
# print(sum)

#투포인터
st = 1
en = 1
ans = 0
while st <= len(num) and en <= len(num):
	if sum[en] - sum[st-1] < n:
		en += 1
	else:
		if sum[en] - sum[st-1] == n:
			ans += 1
		st += 1

print(ans)