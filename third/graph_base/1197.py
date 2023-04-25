#최소 스패닝 트리 : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
#최소 신장 트리 중 크루스칼 알고리즘을 사용한다. 간선이 작기 때문!!
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

def find(x):
    if x != root[x]:
        root[x]=find(root[x])
    return root[x]

v,e = map(int,s.readline().split())
root = [i for i in range(v+1)]
arr=[]
answer=0

for _ in range(e):
    arr.append(list(map(int,s.readline().split())))

arr.sort(key=lambda x:x[2])

for a,b,c in arr:
    ar=find(a)
    br=find(b)
    
    if ar != br:
        if ar>br:
            root[ar] = br
        else:
            root[br]=ar
        
        answer+=c
print(answer)