from sys import stdin as s
from collections import deque

s=open("input.txt","rt")
#2차원 배열 똑바로 하기!!!
n,m = map(int, s.readline().split())
graph=[]
visited = [[False for _ in range(m)] for _ in range(n)] 
dx=[0,1,0,-1]
dy=[1,0,-1,0]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    #bfs는 큐를 이용해서 항상 현재 x,y 값을 저장했다가 빼주고 다음 x,y 값을 저장했다가 뺴준다는 것을 기억할 것
    while queue:
        x,y = queue.popleft()
        visited[x][y]=True
        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]

            if new_x<0 or new_x>=n or new_y<0 or new_y>=m:
                continue
            if graph[new_x][new_y]==0:
                continue
            if graph[new_x][new_y]==1:
                if not visited[new_x][new_y]:
                    graph[new_x][new_y]= graph[x][y]+1
                    visited[new_x][new_y]=True
                    queue.append((new_x,new_y))
            

    return graph[n-1][m-1]    
    
         

for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)

    
print(bfs(0,0))