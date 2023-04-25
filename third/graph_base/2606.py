from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

n=int(s.readline()) #n : 컴퓨터의 수
e = int(s.readline()) #e : 간선의 수
graph=[[] for _ in range(n+1)]
visited = [False] * (n+1)


#bfs 방식으로 풀어보기
def bfs(start):
    count=0
    queue = deque()
    queue.append(start)
    visited[start]=True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                count+=1
                visited[i]=True
                queue.append(i)
           
                
    return count

for i in range(e):
    a,b = map(int,s.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
print(bfs(1))