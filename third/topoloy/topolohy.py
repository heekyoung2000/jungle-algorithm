from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

s=open("input.txt","rt")

v,e = map(int,s.readline().split())
#진입 차수 테이블 초기화
indegree = [0]*(v+1)
#그래프 데이터 담을 인접 리스트 초기화
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b = map(int,s.readline().split())
    graph[a].append(b)
    # 진입 차수 추가 a->b이기 때문에 진입 차수 추가
    indegree[b]+=1

#위상 정렬 함수
def topology_sort():
    result=[] # 알고리즘 수행 결과를 담을 리스트
    q=deque() # 큐 기능을 위한 deque 라이브러리 사용
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        node = q.popleft()
        result.append(node)
        for next in graph[node]:
            #해당 윈소와 연결된 노드들의 진입 차수에서 1 빼기
            indegree[next]-=1
            #새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[next]==0:
                q.append(next)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i,end=' ')
        
topology_sort()
    