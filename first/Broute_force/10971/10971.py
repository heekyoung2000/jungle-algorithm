#DP, 비트마스크 이용
#비트마스크 이용 시 방문한 도시는 1로 방문하지 않은 도시는 0으로 설정
#완전탐색 문제에서는 비트마스크 사용안해도 빈배열 배열 만들어서 지날때마다 증가해주면 됨
import sys
'''n = int(sys.stdin.readline())
new_list=[]
bitmask=[0]*n


def dfs(new_list):
    bitmask=0
    sum=0
    while bitmask<n**2:
        if bitmask == 2**(n-1):#n-1 #d에서 시작할 때
            sum+=min(new_list[n-1])
        elif bitmask == 2**(n-2):#n-2 #b를 지났을 때
            sum+=min(new_list[n-2])
            bitmask+=2**(n-2)
        elif bitmask == 2**(n-3): #n-3 #c를 지났을 때
            sum+=min(new_list[n-3])
            bitmask+=2**(n-3)
        else:  #a를 지났을 때 
            sum+=min(new_list[0])
            bitmask +=1
    return sum
        
            
            
    

for i in range(n):
    list1=list(map(int,sys.stdin.readline().split()))
    new_list.append(list1)
    
dfs(new_list)'''


'''n=int(sys.stdin.readline())
visited = [0]*n
new_list=[]
result = 1e9

def dfs(node, x, cost): #x: 노드를 방문한 횟수 
    global result
    
    if x==n:
        if new_list[node][0]:
            result = min(result, cost+new_list[node][0])
        return
    
    for next_node in range(1,n):
        if new_list[node][next_node] and not visited[next_node]:
            visited[next_node]=True
            dfs(next_node, x+1, cost+new_list[node][next_node])
            visited[next_node]=False
            
            
for i in range(n):
    list1=list(map(int,sys.stdin.readline().split()))
    new_list.append(list1)
    
dfs(0,1,0)
print(result)'''
    
    
    
n = int(sys.stdin.readline())
visited = [0]*n
new_list = []
result = 1e9

def dfs(node,x,cost):
    global result
    
    if x==n:
        if new_list[node][0]:
            result = min(result,cost+new_list[node][0])
        return
    for next_node in range(1,n):
        if not visited[next_node] and new_list[node][next_node]:
            visited[next_node]=True
            dfs(next_node,x+1,cost+new_list[node][next_node])
            visited[next_node]=False
            
for i in range(n):
    list1=list(map(int,sys.stdin.readline().split()))
    new_list.append(list1)
    
dfs(0,1,0)
print(result)
    