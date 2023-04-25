from sys import stdin as s
from collections import deque

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
  
    
    if x<0 or x>=n or y<0 or y>=n: #뱀이 좌표 끝에 닿았을 때 종료
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

        
    
 

#뱀 다시 풀어보기

from sys import stdin as s
from collections import deque

s= open('input.txt','rt')

n=int(s.readline()) #보드의 넓이
k=int(s.readline()) #사과의 개수

graph=[[0]*n for _ in range(n)] 

# 사과 입력받기
for apple in range(k):
    a,b = map(int,s.readline().split())
    graph[a][b]=2 # 사과 위치를 2로 설정

# 방향 변환 정보 입력받기 , 방향을 입력 받을 때 dic에 저장
l = int(s.readline())
dic = dict()
for where in range(l):
    t, w = (s.readline().split()) #t는 시간, w는 방향
    dic[int(t)]=w
    
#초기설정하기 - 뱀의 위치 설정, cnt 설정, deque 설정,x,y 설정,direction 설정
x,y=0,0
graph[x][y]=1
cnt=0
dq=deque()
direction=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#큐에 현재 뱀의 위치 저장
dq.append((0,0))

def changego(dir):
    global direction
    if dir == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

# 여기서 조건 설정- 방향을 옯겨 다니면서 사과를 만난다면, 사과를 만나지 않는다면, 벽을 만난다면, 뱀 자기자신 몸을 만난다면 4가지 경우를 설정한다.
while True:
    # 방향 옮기기, 옮길 때마다 초 추가하기
    cnt+=1
    x+= dx[direction]
    y+= dy[direction]
    
    #벽을 만난다면 실행 종료
    if x<0 or x>=n or y<0 or y>=n:
        break
    
    #뱀이 사과를 만난다면 - 꼬리와 머리의 값을 그대로 남긴다(push만 실행)
    elif graph[x][y]==2:
        graph[x][y]=1
        dq.append((x,y))
        if cnt in dic:
            changego(dic[cnt])
    #뱀이 사과를 안만났을 때 - 꼬리 값을 pop 해주고 머리 값을 push 해줌
    elif graph[x][y]==0:
        graph[x][y]==1
        tx,ty= dq.popleft()
        dq.append((x,y))
        graph[tx][ty]=0 #꼬리부분은 pop 해주고 다시 0으로 초기화
        
        if cnt in dic:
            changego(dic[cnt])
    
    #뱀이 자기자신을 만났거나 이외 다른 경우에는 종료
    else:
        break

print(cnt)