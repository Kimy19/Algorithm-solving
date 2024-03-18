from itertools import combinations
from collections import deque


dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
board = []
store = []
house = []
for i in range(n):
	row = list(map(int,input().split()))
	for j in range(n):
		if row[j] == 2:
			store.append((i,j))
		if row[j] == 1:
			house.append((i,j))
	board.append(row)

#len(store)개 중에서 m개 뽑는 경우의수
arr = [num for num in range(len(store))]
combs = combinations(arr, m)

min = 9999999
for comb in combs:
	dist = []
	for j in range(len(house)):
		hx,hy = house[j]
		temp = 99999
		for i in comb:
			x,y = store[i]
			cal_dist = (abs(hx-x) + abs(hy-y))
			if temp > cal_dist:
				temp = cal_dist
		dist.append(temp)
	if sum(dist)<min:
		min = sum(dist)
print(min)


