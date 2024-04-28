#백준 1655
import heapq
import sys

n = int(input())
ans_list = []
left_heap = [] #max heap
right_heap = [] #min heap
for i in range(1,n+1):
	num = int(sys.stdin.readline())
	if len(left_heap) == len(right_heap):
		heapq.heappush(left_heap,-num)
	else:
		heapq.heappush(right_heap,num)
	if right_heap and left_heap[0]*-1 > right_heap[0]:
		n1 = heapq.heappop(left_heap)
		n2 = heapq.heappop(right_heap)
		heapq.heappush(left_heap,-n2)
		heapq.heappush(right_heap,-n1)
	ans_list.append(left_heap[0])
for i in ans_list:
	print(-i)
