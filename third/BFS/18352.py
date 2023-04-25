from sys import stdin as s
from collections import deque

#1. graph 배열에 노드가 도달할 수 있는 노드 배열로 넣어주기
#2. 방문여부를 체크할 수 있는 visited 빈 배열과 노드마다 최소 거리를 확인 할 수 있는 go_list 배열 만들기
#3. bfs를 사용하여 탐색하기
#3-1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
#3-2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리, 노드를 이동했으므로 현재 노드 값에서 1을 더해준 값을 이동한 노드에 저장함(go_list)
#3-3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복
s=open("input.txt","rt")


def bfs(graph,start,visited,k):
    
    queue = deque()
    queue.append(start) #큐에 시작 값을 넣어줌
    while queue:
        v= queue.popleft()
        visited[start]=True #visited에 방문 값을 true로 바꿔줌
        for i in graph[v]: 
            if not visited[i]: #만약 노드에 방문하지 않았다면
                queue.append(i) #큐에 노드를 추가하고
                visited[i]=True # 방문 true로 해준다음 
                go_list[i] = go_list[v]+1 #간선의 가중치 값을 올려줌

           

n,m,k,x = map(int,s.readline().split()) #n : 도시, m은 간선, k:최단 거리, x : 출발도시
list1 =[]
graph=[[] for _ in range(n+1)]
visited = [False]*(n+1) #방문 여부를 입력해줌
go_list = [0 for _ in range(n+1)] # 간선의 가중치를 저장해줌 
#도달할 수 있는 도시 입력받고 graph 배열에 1,2,3,4 차례로 넣어주기
for i in range(m):
    a,b=map(int,s.readline().split())
    graph[a].append(b)
    graph[a].sort()
bfs(graph,x,visited,k)
    

print(go_list)
                
count=0 #카운트를 설정해서 만약 카운트 값이 k면 count를 계속 해주고 반복이 끝났을 떄 count가 0이면 -1출력
for i in range(1,n+1):
    if go_list[i]==k:
        print(i)
        count+=1
if count ==0:
    print(-1)    
    