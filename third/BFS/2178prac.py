from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n,m=map(int,s.readline().split())
graph=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
        
            if new_x < 0 or new_x >=n or new_y<0 or new_y>=m :
                continue
            if graph[new_x][new_y]==0:
                continue
            if graph[new_x][new_y]==1:
                graph[new_x][new_y]=graph[x][y]+1
                queue.append((new_x,new_y))
   
    return graph[n-1][m-1]


    
print(bfs(0,0))
    

    