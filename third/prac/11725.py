from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
#파이썬에서 기본으로 지원하는 최대 재귀 깊이는 1000인데 노드의 개수가 최대 100,000개 이므로 SETRECURSIONLIMIT사용
#방문 리스트에 부모 노드 값을 저장하도록 설정


s=open("input.txt","rt")
n=int(s.readline())
graph=[[] for _ in range(n+1)]
visited = [0]*(n+1)

def dfs(start):
    for i in graph[start]:
        if visited[i]==0:
            visited[i]=start
            dfs(i)


for i in range(n-1):
    a,b = map(int,s.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)
for i in visited[2:]:
    print(i)