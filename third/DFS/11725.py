from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

n=int(s.readline())
graph =[[] for i in range(n+1)]
visited = [0]*(n+1)
arr=[]

for i in range(n-1):
    a,b=map(int,s.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
def dfs(s):
    for i in graph[s]:
        if visited[i]==0:
            visited[i]=s
            dfs(i)

dfs(1)
print(visited)
for x in range(2,n+1):
    print(visited[x])