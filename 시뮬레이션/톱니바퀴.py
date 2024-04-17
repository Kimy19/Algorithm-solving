# 백준 14891
from collections import deque

q1 = deque()
q2 = deque()
q3 = deque()
q4 = deque()

row = list(map(int,input().strip()))
q1.extend(row)
row = list(map(int,input().strip()))
q2.extend(row)
row = list(map(int,input().strip()))
q3.extend(row)
row = list(map(int,input().strip()))
q4.extend(row)

def printall():
	global q1,q2,q3,q4
	print(q1)
	print(q2)
	print(q3)
	print(q4)

def spin(num, dir):
	global q1,q2,q3,q4

	if num == 1:
		if dir==1:#시계방향
			q1.appendleft(q1.pop())
		else:
			q1.append(q1.popleft())
	elif num == 2:
		if dir==1:#시계방향
			q2.appendleft(q2.pop())
		else:
			q2.append(q2.popleft())
	elif num == 3:
		if dir==1:#시계방향
			q3.appendleft(q3.pop())
		else:
			q3.append(q3.popleft())
	elif num == 4:
		if dir==1:#시계방향
			q4.appendleft(q4.pop())
		else:
			q4.append(q4.popleft())

status = [0,0,0,0,0]
def set_status():
	global status,q1,q2,q3,q4

	if q1[2] != q2[6]:
		status[1] = 1
	else:
		status[1] = 0
	if q2[2] != q3[6]:
		status[2] = 1
	else:
		status[2] = 0
	if q3[2] != q4[6]:
		status[3] = 1
	else:
		status[3] = 0
n = int(input())
for i in range(n):
	set_status()
	print(status)
	printall()
	num,dir = map(int,input().split())
	spin(num,dir)
	temp = num -1
	prev_dir = dir
	#왼쪽으로 확인
	while temp > 0:
		if status[temp]:
			spin(temp, -prev_dir)
		else:
			break
		prev_dir*=-1
		temp-= 1
	temp = num
	prev_dir = dir
	#오른쪽으로 확인
	while temp < 4:
		if status[temp]:
			spin(temp+1,-prev_dir)
		else:
			break
		prev_dir*=-1
		temp+=1
	
ans = 0
if q1[0]:
	ans+=1
if q2[0]:
	ans+=2
if q3[0]:
	ans+=4
if q4[0]:
	ans+=8
print(ans)