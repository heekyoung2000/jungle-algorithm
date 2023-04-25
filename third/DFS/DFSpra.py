from collections import deque
#스택이용- 재귀 이용
def dfs(graph, v, visited):
    visited[v]=True #방문한 노드를 true로 변경
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
       

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
dfs(graph,1,visited)