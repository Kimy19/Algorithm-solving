import heapq
#heapq.heappush
#heapq.heappop
#heapq.heapify

#기본 최소힙
h = []
heapq.heappush(h,5)
heapq.heappush(h,2)
heapq.heappush(h,15)
heapq.heappush(h,3)
print(h)

while (h):
	heapq.heappop(h)
	print(h)

h = [5,3,1,6,7]
heapq.heapify(h)
print(h)

#최대힙 원할 경우 값에 - 처리해서 넣어줄것
h = []
list = [9,3,5,1]
for i in list:
	heapq.heappush(h,i*-1)

for i in h:
	print(i*-1)