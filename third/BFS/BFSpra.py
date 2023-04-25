from sys import stdin as s
from collections import deque
# 큐 이용
#bfs 메서드 정의 
def bfs(graph,start,visited):
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        v= queue.popleft() #큐에서 가장 작은 원소를 pop함
        print(v,end=' ')
        for i in graph[v]: #아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                
                
                
graph = [
    [], # 0번 노드는 비워줌
    [2,3,8], #1번 노드와 연결된 노드
    [1,7], # 2번 노드와 연결된 노드
    [1,4,5], # 3번 노드와 연결된 노드
    [3,5], # 4번 노드와 연결된 노드
    [3,4], # 5번 노드와 연결된 노드
    [7], # 6번 노드와 연결된 노드
    [2,6,8], # 7번 노드와 연결된 노드
    [1,7] # 8번 노드와 연결된 노드
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

bfs(graph,1,visited)

