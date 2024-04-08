import heapq

heap = [] # heap을 리스트로 구현
sz = 0    # heap에 들어있는 원소의 수

def push(x):
    global heap, sz
    heapq.heappush(heap, x) # heapq 모듈의 heappush 함수를 사용하여 원소를 추가
    sz += 1

def top():
    global heap
    if sz == 0:
        return None
    return heap[0] # 최소값은 항상 인덱스 0에 위치함

def pop():
    global heap, sz
    if sz == 0:
        return
    heapq.heappop(heap) # heapq 모듈의 heappop 함수를 사용하여 최소값을 삭제
    sz -= 1

def test():
    push(10); push(2); push(5); push(9) # {10, 2, 5, 9}
    print(top()) # 2
    pop() # {10, 5, 9}
    pop() # {10, 9}
    print(top()) # 9
    push(5); push(15) # {10, 9, 5, 15}
    print(top()) # 5
    pop() # {10, 9, 15}
    print(top()) # 9

n = int(input())
ans = []
# print(top())
for _ in range(n):
	x = int(input())
	if x>0:
		push(x)
	elif x == 0:
		if not heap:
			ans.append(0)
			continue
		ans.append(top())
		pop()
for i in ans:
	print(i)
