## 시간 반복 어떻게 해야 할지 생각해 보기 
##큐에 넣어서 풀어야 한다는 데 다시 생각해보기
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
graph=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]


def bfs(S,x,y,answer):
    queue=deque()
    queue.append((answer,x,y,S))
    queue.sort()
    while queue:
        x,y,time=queue.popleft()
        if time==S:
            return graph
        visited[x][y]=True
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if nx<n and ny<n and graph[nx][ny]==0 and not visited[nx][ny]:
                graph[nx][ny]=answer
                visited[nx][ny]=True
                queue.append((nx,ny,S+1))            
        

n,k=map(int,s.readline().split())
visited = [[False for i in range(n)] for _ in range(n)]

for i in range(n):
    list1=list(map(int,s.readline().split()))
    graph.append(list1)
S,x,y=map(int,s.readline().split())

    
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            result=bfs(S,i,j,graph[i][j])

print(result[i-1][j-1])




    