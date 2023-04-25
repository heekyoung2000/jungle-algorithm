from sys import stdin as s
from collections import deque


#bfs - 큐나 데큐에 저장하여 반복을 돌며 찾아감
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v= queue.popleft()
        print(v,end=' ')
        for i in graph[v]: #아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#dfs - 보통 재귀를 사용
def dfs(graph,start,visited):
    visited[start]=True
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)
    

s=open("input.txt","rt")
#n: 정점의 개수,m: 간선의 개수, v : 탐색을 시작할 정점의 번호
n,m,v = map(int,s.readline().split())
graph=[[] for _ in range(n+1)]
visited_bfs = [False]*(n+1)
visited_dfs = [False]*(n+1) 
# print(graph)



#간선이 연결하는 두 정점의 번호 입력받기 - 간선이 연결하는 두 정점의 번호 갯수를 어떻게 알지..?
for i in range(m):
    a,b = map(int,s.readline().split()) # 1~m-1번노드와 연결되어 있는 노드들을 graph에 저장한다.
    # graph.append([a,b])
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
# print(graph)
dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)



    
