#백준 18870
from bisect import bisect_left

n = int(input())
num = list(map(int,input().split()))

sorted_num = sorted(num)
new_num = []
new_num.append(sorted_num[0])
for i in range(1,len(sorted_num)):
	if sorted_num[i] == sorted_num[i-1]:
		continue
	new_num.append(sorted_num[i])

ans = []
for i in num:
	ans.append(bisect_left(new_num,i))
print(*ans)

