#백준 1991
from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
lc = [0 for _ in range(n+1)]
rc = [0 for _ in range(n+1)]
for _ in range(n):
	i,j,k = map(str,input().split())
	if j != '.':
		lc[ord(i) - 64] = ord(j) - 64
	if k != '.':
		rc[ord(i) - 64] = ord(k) - 64
#전위 순회
ans1 = []
def preorder(cur):
	ans1.append(cur)
	if lc[cur] != 0:
		preorder(lc[cur])
	if rc[cur] != 0:
		preorder(rc[cur])

ans2 = []
#중위 순회
def inorder(cur):
	if lc[cur] != 0:
		inorder(lc[cur])
	ans2.append(cur)
	if rc[cur] != 0:
		inorder(rc[cur])

ans3 = []		
#후위 순회
def postorder(cur):
	if lc[cur] != 0:
		postorder(lc[cur])
	if rc[cur] != 0:
		postorder(rc[cur])
	ans3.append(cur)

preorder(1)
inorder(1)
postorder(1)

for i in ans1:
	print(chr(i + 64), end='')
print()
for i in ans2:
	print(chr(i + 64), end='')
print()
for i in ans3:
	print(chr(i + 64), end='')