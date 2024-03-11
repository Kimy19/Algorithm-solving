#백준 10773
#stack
from collections import deque

q = deque()
n = int(input())

for i in range(n):
	num = int(input())
	if(num != 0):
		q.append(num)
	else:
		q.pop()
print(sum(q))
