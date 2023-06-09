#최소 스패닝 트리 : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
#최소 신장 트리 중 크루스칼 알고리즘을 사용한다. 간선이 작기 때문!!
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
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int,s.readline().split())
parent= [i for i in range(v+1)]
edges = []
result=0

for i in range(1,v+1):
    parent[i]=i
    
    
for _ in range(e):
    a,b,cost=map(int,s.readline().split())
    edges.append((cost,a,b))
    
edges.sort()

for i in range(e):
    cost,a,b=edges[i]
    if find_parent(parent,a)!= find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)
