#다익스트라 알고리즘 사용
#흰방이 1 검은색 방이 0
#시작점에서 출발해서 끝방까지 가는게 목표
#1.방향을 설정해야 하므로 dx,dy를 설정
#2. 가중치,x,y를 설정해주고 만약 끝방위치에 도달했다면 현재 가중치 출력 
#이때 현재 가중치는 검은 벽을 만났을 때 뚫은 갯수
#상하좌우를 돌면서 좌표 설정을 해주는데 1. 벽에 닿지 않았을 때-검은 벽을 만나면 distance에서 1더해줌,흰벽을 만나면 전 distance 값을 그대로 넘겨줌

from sys import stdin as s
from collections import deque
import sys
import heapq
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
n=int(s.readline()) #한줄에 들어가는 방의 수
graph=[]
visited = [[0]*n for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dajistra(cost,x,y):
    q=[]
    heapq.heappush(q,(cost,x,y))
    visited[x][y]=1
    while q:
        a,x,y=heapq.heappop(q)
        if x==n-1 and y==n-1:
            print(a)
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                if graph[nx][ny]==0:
                    heapq.heappush(q,(a+1,nx,ny))
                else:
                    heapq.heappush(q,(a,nx,ny))
    


for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)
dajistra(0,0,0)
    
