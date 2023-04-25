from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n= int(s.readline())
top_list = list(map(int,s.readline().split()))
dq=deque()

stack=[0]*n #0으로 초기화된 배열 선언

def razor(dq):
    for i in range(len(top_list)):
        while dq and dq[-1][0]<top_list[i] : dq.pop()
        
        if dq: stack[i] = dq[-1][1]
        dq.append((top_list[i],i+1))
    
    print(* stack)
razor(dq)


