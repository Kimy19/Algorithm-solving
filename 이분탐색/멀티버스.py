# baekjoon 18869
import sys
from bisect import bisect_left,bisect_right

m,n = map(int,input().split())
num = {}
for _ in range(m):
	row = list(map(int,input().split()))
	s_row = sorted(row)
	temp =[]
	for i in row:
		l = bisect_left(s_row,i)
		temp.append(l)
	key = tuple(temp)
	if key in num:
		num[key] += 1
	else:
		num[key] = 1

count = 0
for i in num.values():
	if i > 1:
		count += i * (i-1) // 2 
print(count)
