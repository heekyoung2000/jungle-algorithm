from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
graph=[]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if graph[x][y] == '-':
            graph[x][y] = "1"
            if y+1 <m and graph[x][y+1]=='-':
                queue.append((x,y+1))
        elif graph[x][y]=="|":
            graph[x][y]="1"
            if x+1 < n and graph[x+1][y]=="|":
                queue.append((x+1,y))
    
n,m=map(int,s.readline().split()) #m:가로 크기, n:세로크기
cnt=0
for i in range(m):
    list1=list(map(str,s.readline().strip()))
    graph.append(list1)
    
for i in range(n):
    for j in range(m):
        if graph[i][j]!="1":
            bfs(i,j)
            cnt+=1
print(cnt)