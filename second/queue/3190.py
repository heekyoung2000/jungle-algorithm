from sys import stdin as s
from collections import deque

where_k=[] # 사과의 위치 정보 저장
where_go=[] #뱀의 방향 변롼 정보 저장
s=open('input.txt','rt')


n=int(s.readline()) #보드의 크기
k=int(s.readline()) #사과의 개수

graph=[[0]* n for _ in range(n)] #graph 배열을 0으로 초기화 해줌
dx = [0,1,0,-1] #x축 방향 이동 할때 (오른쪽 왼쪽 포함)
dy= [1,0,-1,0] #y축 방향 이동 할때 (위로 아래로 포함)

for i in range(k): #사과의 위치 저장하기
    a,b = map(int,s.readline().split())
    graph[a-1][b-1]=2 #사과 위치에는 값을 2로 저장 

l = int(s.readline()) #뱀의 방향 변환 횟수
dirDict = dict() #딕셔너리 선언
queue = deque() #큐 선언
queue.append((0,0)) #큐에 뱀 출발 지점 push

for j in range(l):
    x,c = (s.readline().split()) 
    dirDict[int(x)]=c #딕셔너리 key: 시간, value : 방향
    print(dirDict)
    
x,y = 0,0
graph[x][y] =1 # 좌표 0,0에 뱀이 존재하므로 1로 설정 
cnt =0 # 몇초 지났는지 카운트
direction = 0 #방향 초기화

def turn(alpha): 
    global direction
    if alpha == 'L': #방향이 L일 경우 
        direction = (direction-1)%4
    else: #방향이 R일 경우
        direction = (direction+1)%4

while True:
    cnt+=1
    x+= dx[direction]
    y+= dy[direction]
    print(x,y)
    
    if x<0 or x>=n or y<0 or y>=n:
        break
    
    if graph[x][y]==2: #만약 사과를 만났을 경우
        graph[x][y]=1 # 뱀이 위치한 자리를 1로 바꿔주고
        queue.append((x,y)) #큐에 x,y 저장
        if cnt in dirDict:
            turn(dirDict[cnt])
    elif graph[x][y]==0: #만약 사과를 만나지 않았을 경우
        graph[x][y]=1 #뱀이 위치한 자리를 1로 바꿔줌
        queue.append((x,y)) #큐에 x,y 저장
        tx,ty = queue.popleft() #뱀의 꼬리 pop 하기
        graph[tx][ty]=0 #뱀의 꼬리가 빠진 부분은 다시 0으로 만들어주기
        if cnt in dirDict: #만약 cnt 초가 배열안에 있다면 
            turn(dirDict[cnt]) #방향 바꿔주기로 재귀함수 돌림

    else:
        break
print(cnt)    

        
    
 
