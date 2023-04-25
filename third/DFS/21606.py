# 실외를 가운데에 놓고 설정할 것

#1. 실외를 거치는 경우
    # 1-1. 실회가 하나인 경우 : 
#2. 실외를 거치지 않는 경우
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
n=int(s.readline())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
location = list(map(int,list("0"+s.readline().strip())))#각 노드가 실내(1)인지 실외(0)인지 저장한 문자열, 이때 노드 번호를 index에 접근하기 위해 앞에 0추가
sum=0

for _ in range(n-1):
    u,v= map(int,s.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    if location[u] ==1 and location[v]==1: #둘다 실내 일 경우 
        sum+=2 #서로 방문하는 케이스가 2가지이나 바로 2개 세기
    

def dfs(start):
    """ graph : 노드와 간선을 저장 """
    visited[start] = True
    cnt=0
    for i in graph[start]:
        #실외가 하나일 경우
        if location[i] == 1:# 인접한 노드가 실내라면
            cnt+=1 #실내 노드 개수를 증가
        #실외가 두개 이상인경우    
        elif not visited[i] and location[i]==0: #그 노드에서부터 탐색하여 실내 노드 개수 증가
            cnt+= dfs(i)
    return cnt #실내 노드 개수 반환




for i in range(1,n+1):
    if not visited[i] and location[i]==0: #시작이 실외일떄만 발생
        result=dfs(i)#dfs를 통해 인접한 실내 노드 개수를 계산
        sum+=result*(result-1) #경로의 개수 추가
  
print(sum)

