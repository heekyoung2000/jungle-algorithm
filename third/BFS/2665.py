import heapq  # 우선순위 큐 구현을 위함
from sys import stdin as s

s=open("input.txt","rt")

n=int(s.readline()) # 한줄에 들어가는 방의 수
graph=[]
INF = int(1e9)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
distance = [[INF]*n for _ in range(n)]

def daijistra(x,y,d): #x: x 좌표, y: y좌표, d : 가중치
    hq=[]
    heapq.heappush(hq,(x,y,d))
    distance[x][y]=d
    while hq:
        now_d,now_x,now_y = heapq.heappop(hq)
        if now_x == n-1 and now_y == n-1:
            print(now_d)
            break
        for i in range(4):
            nx=now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx < n and 0<=ny<n and distance[nx][ny]>now_d+1:
                if graph[nx][ny]==0: # 검은 벽이라면 전 distance에서 1 더해줌
                    distance[nx][ny]=min(distance[nx][ny],now_d+1)
                else: #흰벽이라면 전 distance값을 넘겨줌
                    distance[nx][ny] = min(distance[nx][ny],now_d)
                heapq.heappush(hq,(distance[nx][ny],nx,ny))
    
    

for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)
    
daijistra(0,0,0)

