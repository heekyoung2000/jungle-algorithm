#bfs 반복해야 하는데 반복이 안됨
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y):
    cnt=1 #x,y의 좌표에서 1값일 떄를 추가해줘야 해서 1로 시작
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    visited[nx][ny]=True
                    continue
                elif graph[nx][ny]==1:
                    if not visited[nx][ny]:
                        cnt+=1
                        visited[nx][ny]=True
                        queue.append((nx,ny))
    return cnt


n=int(s.readline())
visited=[[False for i in range(n)]for i in range(n)]
graph=[]
for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)

count=0
group=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            result=bfs(i,j)
            group.append(result)
            count+=1

group.sort()
print(count)
for i in group:
    print(i)

# total=0
# group=[]
# for i in range(n):
#     result=bfs(i,i)
#     if result!=0:
#         total+=1
#         group.append(result)
# group.sort()
# print(total)
# for j in group:
#     print(j)