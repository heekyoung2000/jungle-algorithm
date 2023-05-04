#가중치를 이용한 최단 경로를 구해야 하므로 다익스트라 알고리즘을 사용해야 함
#우선순위 힙을 이용해서 구해야함
#우선순위 힙 : 시작 노드와 시작값(0)을 우선순위 큐에 넣는다.
#[inf]*(n-1) 무제한 배열?을 선언한다.
#무제한배열에 인덱스 시작 노드 값을 0으로 선언한다.
#우선순위 큐가 비지 않을 동안, 삽입된 큐를 빼서 현재 노드의 값이 distance에 저장되어 있는 값보다 더 크면 비교가 필요 없으므로 continue
#그래프에서 현재 값과 새로운 노드를 거쳐갈때의 거리를 더한 값을 알고 있는 값보다 작으면 갱신하고 큐에 삽입한다.
from sys import stdin as s
from collections import deque
import heapq
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
INF = int(1e9)



n=int(s.readline())
m=int(s.readline())
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

def dijkstra(start):
    distance[start] =0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        current_cost,current_node = heapq.heappop(q)
        
        if distance[current_node]<current_cost:
            continue
        for new_cost,new_node in graph[current_node]:
            cost = current_cost+new_cost
            if cost<distance[new_node]:
                distance[new_node]=cost
                heapq.heappush(q,(cost,new_node)) 
        
    return cost
        

for i in range(m):
    a,b,cost=map(int,s.readline().split())
    graph[a].append((cost,b))
    
start,end= map(int,s.readline().split())
print(dijkstra(start))
