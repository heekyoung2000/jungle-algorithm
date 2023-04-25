#힙 정렬 알고리즘

'''def down_heap():
    temp = a[left]
    
    parent=left
    while parent < (right+1)//2:
        cl = parent *2 +1
        cr = cl+1
        child = cr if cr <= right and a[cr]>a[cl] else cl
        if temp >= a[child]:
            break
        a[parent] = a[child]
        parent = child
    a[parent] = temp
    
n=len(a)
for i in range((n-1)//2,-1,-1):
    down_heap(a,i,n-1)

for i in range(n-1,0,-1):
    a[0],a[i]=a[i],a[0]
    down_heap(a,0,i-1)
    
for i in range(num):
    heap_sort(i)    

'''
#계산기
'''import sys
​
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}
​
def join_array(ints):
    str_list = list(map(str, ints))
    return " ".join(str_list)
​
class ArrayStack:
    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.size() == 0


    def push(self, item):
        self.data.append(item)
​   
    def pop(self):
        return self.data.pop()
​
    def peek(self):
        return self.data[-1]
​
    def serialize(self):
        return join_array(self.data)
​
​
def convert_to_postfix(S):
    opStack = ArrayStack()
    answer = ''
    
    for w in S :
        if w in prec :
            if opStack.isEmpty() :
                opStack.push(w)
            else :
                if w == '(' :
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) :
                        answer += opStack.pop()
                        if opStack.isEmpty() : break
                    opStack.push(w)
        elif w == ')' :
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop()
        else :
            answer += w
        
    while not opStack.isEmpty() :
        answer += opStack.pop()
    
    return answer
​
def calculate(tokens):
    stack = ArrayStack()
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop())
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.push(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()//rv)
        else:
            stack.push(int(token))
        
    return stack.pop()
​
# infix 수식에서 공백 제거
infix = sys.stdin.readline().replace("\n", "").replace(" ", "")
​
postfix = convert_to_postfix(infix)
​
print(f"postfix : {postfix}")
​
result = calculate(postfix)
​
print(f"result : {result}")
​'''

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