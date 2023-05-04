#경우의 수: 실외를 거치는 경우- 실외기가 하나인 경우
#실외가 두개 이상인 경우, 실외가 떨어져있는 경우
#실외를 거치지 않는 경우: 실내-실내인 경우 2가지
#경우의 수 n*n-1을 할때 n은 실내기의 갯수이다.
#1.graph와 visited 방문 리스트를 설정한다. 정점의 수를 입력받고 문자열을 입력받는데 이때 노드 번호를 index에 접근하기 위해 앞에 0추가
#2. 간선 정보를 저장 이때 둘다 실내일 경우 서로 방문하는 케이스가 2가지 이므로 sum변수에 2더하기
#3. 방문하지 않았을 경우와 시작이 실외 일때 - dfs를 통해 인접한 실내 노드 개수를 계산
#3-1.dfs- 현재 노드에 방문 처리 해주고 인접한 노드가 실내라면 cnt+=1을 시행
#3-2.dfs- 만약 방문하지 않은 노드에 인접한 노드가 실외라면 실외에 인접한 실내 노드를 찾기 위해 다시 dfs 수행하고 그 값을 cnt에 더해줌 
from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)
s=open("input.txt","rt")
n=int(s.readline())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
sum=0

def dfs(start):
    visited[start]=True
    cnt=0
    for i in graph[start]:
        if list1[i]==1:
            cnt+=1
        elif not visited[i] and list1[i]==0:
            cnt+=dfs(i)
    return cnt
    

list1 = list(map(int,list("0"+s.readline().strip()))) # 주어진 문자열-노드번호로 접근하기 위해 앞에 0 추가
for i in range(n-1):
    u,v=map(int,s.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    if list1[u]==1 and list1[v]==1: #둘다 실내 일 경우
        sum+=2
    
for i in range(1,n+1):
    if not visited[i] and list1[i]==0:
        result=dfs(i)
        sum+=result*(result-1) #경로의 개수의 경우의 수가 n*n-1
print(sum)       