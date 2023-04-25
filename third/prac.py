from sys import stdin as s
from collections import deque

# def dfs(graph,v,visited_dfs):
#     visited_dfs[v]=True
#     print(v,end= ' ')
#     for i in graph[v]:
#         if not visited_dfs[i]:
#             dfs(graph,i,visited_dfs)
            
# def bfs(graph,v,visited_bfs):
#     queue = deque([v])
#     visited_bfs[v]=True
#     while queue:
#         v=queue.popleft()
#         print(v,end=' ')
#         for i in graph[v]:
#             if not visited_bfs[i]:
#                 queue.append(i)
#                 visited_bfs[i]=True
        
            
    

# s=open("input.txt","rt")
# n,m,v = map(int,s.readline().split())
# graph = [[] for _ in range(n+1)]
# visited_dfs=[False]*(n+1)
# visited_bfs=[False]*(n+1)

# for i in range(m):
#     a,b=map(int,s.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     graph[a].sort()
#     graph[b].sort()

# dfs(graph,v,visited_dfs)
# print()
# bfs(graph,v,visited_bfs)

#다익스트라 알고리즘 사용 - 최소 힙
import heapq
from sys import stdin as s
s=open("input.txt","rt")

INF = int(1e9) 
n,m = map(int,s.readline().split())
start = int(s.readline())
graph = [[] for i in range(n+1)]
distance = [INF] *(n-1)

for _ in range(m):
    a,b,c = map(int,s.readline().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance=[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                


