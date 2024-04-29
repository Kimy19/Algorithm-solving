# 백준 13335
from collections import deque

n,w,l = map(int,input().split())
truck = list(map(int,input().split()))

time = 0
bridge = [0 for _ in range(w)]
while bridge:
    time+= 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= l:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)