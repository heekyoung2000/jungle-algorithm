#다익스트라 알고리즘(개선 전)

from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

n,m = map(int, s.readline().split())
start = int(s.readline())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF] * (n+1) #최단 거리 테이블을 모두 무한을 초기화

for _ in range(m):
    a,b,c =map(int,s.readline().split())
    graph[a].append((b,c))
    
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=1
        return index
    
def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now]=True
        for j in range(n-1):
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]]=cost
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
    
#다익스트라 알고리즘(개선 후) - 최소 힙 사용
import heapq
from sys import stdin as s
s=open("input.txt","rt")

INF = int(1e9)

n,m = map(int, s.readline().split())
start= int(s.readline())
graph = [[] for i in range(n+1)]
distance = [INF] *(n-1)

for _ in range(m):
    a,b,c = map(int, s.readline().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #q에 0,start 값을 넣어줌
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q) #최단 거리가 가장 짧은 노드를 추출
        if distance[now] < dist: #현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        # 현재 처리 중인 노드와 인접한 노드 확인
        for i in graph[now]:
            cost= dist + i[1]
            if cost < distance[i[0]]: #현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우
                distance[i[0]] = cost #최단 거리 테이블 갱신
                heapq.heappush(q,(cost,i[0])) #우선순위 큐에 (거리, 노드) 삽입
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])