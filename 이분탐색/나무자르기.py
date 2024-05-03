#baekjoon 2805
import sys

n,m = map(int,sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))

max_h = max(h)
min_h = 0
ans = 0
while(min_h <= max_h):
	sum = 0
	height = (max_h + min_h) // 2
	for i in h:
		if height < i:
			sum += i - height
	if sum >= m:
		min_h = height + 1
	else:
		max_h = height - 1

print(max_h)