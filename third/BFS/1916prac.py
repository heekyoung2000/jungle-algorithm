#최소 비용을 구해야 하므로 다익스트라의 최소 힙을 사용해야 함

from sys import stdin as s
from collections import deque
import heapq

s=open("input.txt","rt")

# def bfs(start,end,)
# INF = int(1e9)
# n = int(s.readline())
# m=int(s.readline())
# graph=[[] for _ in range(n+1)]
# distance = [INF]*(n+1)
    
# for i in range(m):
#     st,e,v= map(int,s.readline().split())
#     graph[st].append((v,e)) #heapq를 비용 기준으로 활용할 계획

# start,end = map(int,s.readline().split())

# def dijkstra(graph,start):
#     q=[]
#     heapq.heappush(q,(0,start))
#     distance[start]=0
#     while q:
#         dist, node = heapq.heappop(q)
#         if distance[node] < dist:
#             continue
#         for next_node,next_dist in graph[node]:
#             cost=dist+next_dist
#             if cost<distance[next_node]:
#                 distance[next_node]= cost
#                 heapq.heappush(q,(cost,next_node))
#     return distance

# dist_start= dijkstra(graph,start)
# print(dist_start[end])

n=int(s.readline())
m=int(s.readline())
graph=[[] for _ in range(n)]

for i in range(m):
    a,b,c=map(int,s.readline().split())
    graph[a].append((b,c))

start,end= map(int,s.readline().split())
    
def bfs(graph,start):
    distances = [int(1e9)] * (n+1)
    distances[start]=0
    queue = []
    heapq.heappush(queue,[distances[start],start])
    
    while queue:
        dist,node = heapq.heappop(queue)
        
        if distances[node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:
            distance = dist+next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
        
    return distances

dist_start = bfs(graph,start)
print(dist_start[end])
            
    


print(graph)