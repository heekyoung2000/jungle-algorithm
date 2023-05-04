#비트마스크 사용 dp 사용
#dfs 를 사용해서

#갈수 없는 경우 무한대 반환
# 이전에 계산된 경우 결과 반환
# 비용이 0이어서 갈 수 없거나, 이미 방문한 루트면 무시
# 현재 도시까지 방문한 경우 중에서 최소 비용이 드는 루트의 비용, 현재 도시까지 방문하는 비용 리턴
from sys import stdin as s
from collections import deque
s=open("input.txt","rt")
n=int(s.readline())
world =[]
for _ in range(n):
    world.append(list(map(int,s.readline().split())))
    
dp={}

def DFS(now, visited):
    #모든 도시를 방문한 경우, 
    if visited == (1<<n)-1:
        #다시 출발 도시로 갈 수 있는 경우 출발 도시까지의 비용을 반환
        if world[now][0]:
            return world[now][0]
        else:
            return int(1e9)
        
    if (now,visited) in dp:
        return dp[(now,visited)] #now까지 방문한 최소 비용
    
    min_cost = int(1e9)
    for next in range(1,n):
        if world[now][next] == 0 or visited & (1<<next):
            continue
        cost=DFS(next, visited | (1<<next))+world[now][next]
        min_cost = min(cost,min_cost)
    
    dp[((now,visited))]=min_cost
    return min_cost
print(DFS(0,1))
        

