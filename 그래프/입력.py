#그래프 입력방법

v,e = map(int,input().split())
board = [[0 for _ in range(v)] for _ in range(v)]

#입접 행렬 O(V^2)
#간선이 V^2에 가까울때, 두정점의 연결여부 확인시 효율적
for _ in range(e):
	i,j = map(int,input().split())
	board[i][j] = 1
	#무방향그래프일 경우
	board[j][i] = 1

#인접 리스트 O(V+E)
#간선이 V^2보다 작을때, 한정점과 연결된 모든 정점 확인시 효율적
board = [[] for _ in range(v)]
for _ in range(e):
	i,j = map(int,input().split())
	board[i].append(j)
	#무방향일 경우
	board[j].append(i)