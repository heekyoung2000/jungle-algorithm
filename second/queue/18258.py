from sys import stdin as s
from collections import deque

dq = deque() #덱 생성

def deq(n):
    if n[0]=="push":
        dq.append(n[1])
    elif n[0]=="front":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0]) #가장 앞에 있는 정수 출력
    elif n[0]=="back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1]) #가장 뒤에 있는 정수 출력
    elif n[0]=="size":
        print(len(dq))
    elif n[0]=="empty":
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif n[0]=="pop":
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())

s=open('input.txt','rt')
n = int(s.readline())
for i in range(n):
    no=list(map(str,s.readline().split()))
    deq(no)