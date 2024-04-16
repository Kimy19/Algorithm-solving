#백준 2075
import heapq

n = int(input())
arr = []
for _ in range(n):
	row = list(map(int,input().split()))
	if not arr:
		for item in row:
			heapq.heappush(arr,item)
	else:
		for item in row:
			if arr[0] < item:
				heapq.heappop(arr)
				heapq.heappush(arr,item)
print(arr[0])

