#옆으로 이동
#아래로 이동
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
graph=[]
dx=[1,0]
dy=[0,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        #옆으로 이동->y+1
        #옆으로 인접한 노드가 있으면 하나의 나무판자로 판단한다.
        if graph[x][y]=='-':
            graph[x][y]="1"
            if y+1<n and graph[x][y+1]=='-':
                queue.append((x,y+1))
        
        #아래로 이동->x+1
        #아래로 인접한 노드가 있으면 하나의 나무판자로 판단한다.
        elif graph[x][y]=='|':
            graph[x][y]="1"
            if x+1<m and graph[x+1][y]=='|':
                queue.append((x+1,y))
        

m,n=map(int,s.readline().split()) #m:가로 크기, n:세로크기
visited = [[0 for i in range(n)] for i in range(m)]
for i in range(m):
    list1=list(map(str,s.readline().strip()))
    graph.append(list1)

cnt=0
for i in range(m):
    for j in range(n):
        if graph[i][j]!="1":
            bfs(i,j)
            cnt+=1

print(cnt)

    

