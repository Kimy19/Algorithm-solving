#baekjoon 2630
import sys

n = int(input())
board = []
for _ in range(n):
	row = list(map(int,input().split()))
	board.append(row)

# print(map)
white = 0
blue = 0
def cut(x,y,n):
	global white,blue

	color = board[x][y]
	for i in range(x,x+n):
		for j in range(y, y+n):
			if board[i][j] != color:
				cut(x,y,n//2)
				cut(x+n//2,y,n//2)
				cut(x,y+n//2,n//2)
				cut(x+n//2,y+n//2,n//2)
				return
	if color == 0:
		white += 1
	else:
		blue += 1
cut(0,0,n)
print(white)
print(blue)