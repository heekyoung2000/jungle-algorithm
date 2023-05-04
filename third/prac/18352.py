from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")


# 방문한 노드에 간선 값 저장해주는 방법 사용
# 큐에 저장하는 거 기억하기 

n,m,k,x = map(int,s.readline().split())
graph=[[] for _ in range(n+1)]
visited = [False]*(n+1)
go_list=[0]*(n+1)

def bfs(x):
    queue=deque()
    queue.append(x)
    while queue:
        v=queue.popleft()
        visited[v]=True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                go_list[i]=go_list[v]+1
        
    return go_list

for i in range(m):
    a,b=map(int,s.readline().split())
    graph[a].append(b)

list1=bfs(x)
cnt=0
for i in range(len(list1)):
    if list1[i]==k:
        print(i)
        cnt+=1
if cnt==0:
    print(-1)