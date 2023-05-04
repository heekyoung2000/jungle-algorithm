from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

n=int(s.readline())

def dfs(start,group):
    visited[start] =group #현재 노드의 그룹 저장
    
    #인접 노드 탐색
    for v in graph[start]:
        if visited[v]==0:
            result = dfs(v,-group) #-group : 현재 노드의 그룹과 다른 값 전달
            if not result:
                return False        
        else:
            if visited[v] == group:
                return False
    return True


for _ in range(n):
    v,e = map(int,s.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        a,b = map(int,s.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    for i in range(1, v+1):
        if visited[i] ==0: #각각 떨어져 있는 노드에 대해서도 이분그래프 인지 판별해줘야 하기 때문에 for문 돌림
            result = (dfs(i,1))
            if not result:
                break
        
    if result:
        print("YES")
    else:
        print("NO")
    

    