from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

n,m = map(int,s.readline().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,s.readline().split())
    graph[a].append(b)
    indegree[b]+=1
    print(indegree)
    
def topology_sort():
    result=[]
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
        
    while q:
        node = q.popleft()
        result.append(node)
        for next in graph[node]:
            indegree[next]-=1
            print(indegree)
            if indegree[next]==0:
                q.append(next)
                
    for i in result:
        print(i,end=' ')
        
topology_sort()