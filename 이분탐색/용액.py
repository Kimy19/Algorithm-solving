#baekjoon 2467
import sys
from bisect import bisect_left,bisect_right

n = int(input())
num = list(map(int,input().split()))
num = sorted(num)
length = len(num)
ans = [num[0],num[1]]
value = abs(num[0] + num[1])
for i in range(length):
	index = bisect_right(num,-num[i])
	l = index -1
	r = index
	if l >= 0 and l<length and l != i:
		if abs(num[i] + num[l]) < value:
			value = abs(num[i] + num[l])
			ans = [num[i],num[l]]
	if r >= 0 and r<length and r != i:
		if abs(num[i] + num[r]) < value:
			value = abs(num[i] + num[r])
			ans = [num[i],num[r]]
print(*sorted(ans))