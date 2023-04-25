from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n,m,k,x=map(int,s.readline().split()) #n:노드의 개수, m: 간선의 개수, k: 최단 거리, x: 출발 도시의 번호
graph=[[] for _ in range(n+1)]
visited = [False] * (n+1)
go_list=[0 for _ in range(n+1)] 

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        visited[x]=True
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                go_list[i]=go_list[v]+1 #누적합으로 합을 계속 더해줘야 하므로 현재 값에서 1씩 더해준 다음 다음값에 저장해준다.(틀린부분)
                
    
for i in range(m):
    a,b=map(int,s.readline().split())
    graph[a].append(b)
    graph[a].sort()


bfs(x)

count=0
for i in range(1,n+1):
    if go_list[i]==k:
        print(i)
        count+=1
if count==0:
    print(-1)
    
    