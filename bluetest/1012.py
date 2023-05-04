from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
dx=[0,1,0,-1]
dy=[1,0,-1,0]



def bfs(x,y):
    count=0
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]
            if new_x<0 or new_x>=n or new_y<0 or new_y>=m:
                continue
            if graph[new_y][new_x]==0:
                continue
            if graph[new_y][new_x]==1:
                if not visited[new_x][new_y]:
                    queue.append((new_x,new_y))
                    queue.append([new_y,new_x])
        count+=1
                
                # queue.append((new_x,new_y))
    return count
                
    
    
    

T=int(s.readline())
for i in range(T):
    m,n,k=map(int,s.readline().split()) #m:가로, n:세로, k: 배추의 위치의 개수
    graph=[[0 for _ in range(n)] for i in range(m)]
    visited=[[False for _ in range(n)] for i in range(m)]
    for i in range(k):
        x,y= map(int,s.readline().split())
        graph[x][y]=1 #x:가로 y:세로
    
print(bfs(0,0))

