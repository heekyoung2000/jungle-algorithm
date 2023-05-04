from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

#1. find연산 정의하기
#2. union 연산 정의하기
#3. 간선과 노드 입력 받고 부모 인접 리스트 생성하고, 간선리스트 만들기
#4. 부모 인접 리스트에 자기 자신을 저장하기
#5. 출발 노드와 끝나는 노드, cost 입력받고 간선리스트에 추가하고 정렬하기
#6. 만약 부모 인접리스트에 저장되어 있는 값이 a,b가 서로 다르다면 union 합수 호출하고 result에 비용 더하기

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e = map(int,s.readline().split())
parent= [i for i in range(v+1)]
edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i
    
for _ in range(e):
    a,b,cost=map(int,s.readline().split())
    edges.append((cost,a,b))
    
edges.sort()

for i in range(e):
    cost,a,b=edges[i]
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result+=cost
print(result)
    