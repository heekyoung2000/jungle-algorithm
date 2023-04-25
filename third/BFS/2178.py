from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n,m=map(int,s.readline().split())

graph=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#배열 입력 받기
for i in range(n):
    list1= list(map(int,s.readline().strip()))
    graph.append(list1)

def bfs(x,y):
    #현재 노드를 방문 처리
    queue=deque()
    queue.append((x,y)) #현재 큐에 x,y 값을 저장
    while queue: #큐가 도는동안
        x,y=queue.popleft() #처음 x,y 값을 popleft로 빼면서 x,y에 저장
    #상하좌우를 돌면서 새로운 좌표 처리
        for i in range(4):
            new_x = x+dx[i] 
            new_y = y+dy[i] 
            
            #만약 배열을 넘어선다면 무시
            if new_x< 0 or new_x >= n or new_y<0 or new_y>=m:
                continue
            #만약 그래프에서 0을 만난다면 무시
            if graph[new_x][new_y]==0:
                continue
            #만약 그래프가 1일 경우 현재 노드에 1씩 추가하면서 이동
            if graph[new_x][new_y]==1:
                graph[new_x][new_y] = graph[x][y]+1
                queue.append((new_x,new_y)) #새로운 x,y를 추가하여 queue에 저장
    return graph[n-1][m-1]
    
print(bfs(0,0))