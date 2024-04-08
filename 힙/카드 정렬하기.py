# 백준 1715
import sys
import heapq

h = []
n = int(input())
for i in range(n):
	num = int(sys.stdin.readline())
	heapq.heappush(h,num)

ans = 0
while 1:
	if len(h) == 1:
		break
	temp1 = heapq.heappop(h)
	temp2 = heapq.heappop(h)
	ans += temp1+temp2
	heapq.heappush(h,temp1+temp2)

print(ans)
