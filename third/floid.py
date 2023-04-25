#n의 갯수가 많을 수록 불리 -> 시간 복잡도 o(n3)

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

#노드의 개수 및 간선의 개수를 입력받기
n=int(input())
m=int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
            
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a,b,c= map(int, input().split())
    graph[a][b]=c
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINTY",end =" ")
        else:
            print(graph[a][b],end= " ")
            
    print()