import heapq  # 우선순위 큐 구현을 위함
from sys import stdin as s

s=open("input.txt","rt")
#1.방향을 설정해야 하므로 dx,dy를 설정
#2. 가중치,x,y를 설정해주고 만약 끝방위치에 도달했다면 현재 가중치 출력 
#이때 현재 가중치는 검은 벽을 만났을 때 뚫은 갯수
#상하좌우를 돌면서 좌표 설정을 해주는데 1. 벽에 닿지 않았을 때-검은 벽을 만나면 distance에서 1더해줌,흰벽을 만나면 전 distance 값을 그대로 넘겨줌

n=int(s.readline()) # 한줄에 들어가는 방의 수
graph=[]
INF = int(1e9)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visit=[[0]*n for _ in range(n)]

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, 0])
    visit[0][0] = 1
    while q:
        a, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if graph[nx][ny] == 0:
                    heapq.heappush(q, [a + 1, nx, ny])
                else:
                    heapq.heappush(q, [a, nx, ny])
    
    

for i in range(n):
    list1=list(map(int,s.readline().strip()))
    graph.append(list1)
    
dijkstra()

