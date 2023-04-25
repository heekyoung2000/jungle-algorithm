from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
INF= int(1e9) #무한대 값

s=open("input.txt","rt")

v,e=map(int,s.readline().split()) #v : 정점의 개수  #e : 간선의 개수
edges = [] # 모든 간선에 대한 정보를 담는 리스트
distance = [INF] * (v+1)
def bellmanford(start):
    #시작 노드에 대해서 초기화
    distance[start]=0
    for i in range(v):
        for j in range(e):
            curNode, nextNode, edgeCost = edges[j]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[curNode] != INF and distance[curNode]+edgeCost < distance[nextNode]:
                distance[nextNode] = distance[curNode]+edgeCost
                #v번쨰 반복에서 갱신되는 값이 있으면 negative cycle 존재
                if i == v-1:
                    return False
    return True
    
for i in range(e):
    a,b,c= map(int,s.readline().split()) #A: 정점, B: 정점, C: 가중치
    edges.append((a,b,c))
    
if bellmanford(1):
    for i in range(2,v+1):
        if distance[i]!=INF:
            print(distance[i])

    