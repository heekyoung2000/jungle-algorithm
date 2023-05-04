# n,m 크기 만큼 배열 받아서 그래프에 저장
# 근처 노드를 계속 탐색해야 하므로 bfs 시행
# dx,dy를 지정함
# 0,0부터 앞,뒤,양 옆으로 탐색해주어야 함
# 큐를 설정하고 처음 시작 위치인 0,0을 넣어준다.
# queue에 처음 저장된 x,y 값을 pop해서 x,y에 저장한다.
# 방문여부를 꼭 체크할것!!!!!! -> 이것때문에 자꾸 오류남-> 방문 표시 어디에다가 해줘야 할지 정확하게 파악할것!!!!!
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")

n,m=map(int,s.readline().split())
graph=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visited=[[False for i in range(m)] for i in range(n)]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x<0 or new_x>=n or new_y<0 or new_y>=m:
                continue
            if graph[new_x][new_y]==0:
                continue
            if graph[new_x][new_y]==1:
                if not visited[new_x][new_y]:
                    queue.append((new_x,new_y))
                    graph[new_x][new_y]=graph[x][y]+1
    return graph[n-1][m-1]
        
    
    

for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)
    
print(bfs(0,0))