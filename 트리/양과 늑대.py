from collections import deque
import sys
import copy

sys.setrecursionlimit(10000000)

max_ans = 0
def find_path(graph,info, cur, next, visit, sheep,wolf):
    global max_ans
    
    if info[cur] == 0:
        sheep += 1
    else:
        wolf -= 1
    if sheep-wolf <= 0:
        return
    max_ans = max(max_ans, sheep)
    temp = copy.deepcopy(next)
    print(temp)
    for i in graph[cur]:
        if visit[i] == 0:
            temp.append(i)
    for _ in range(len(temp)):
        i = temp.popleft()
        visit[i] = 1
        find_path(graph,info,i,temp,visit,sheep,wolf)
        temp.append(i)
        visit[i] = 0

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for i in edges:
        s,e = i
        graph[s].append(e)
        
    next = deque()
    visit = [0 for _ in range(len(info))]
    visit[0] = 1
    find_path(graph, info, 0, next, visit, 0,0)
        
    return max_ans

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))
