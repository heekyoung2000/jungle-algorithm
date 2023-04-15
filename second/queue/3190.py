from sys import stdin as s
from collections import deque

s=open('input.txt','rt')
n=int(s.readline())
dq=deque()
list1=[]
def lazor(dq):
    for j in range(len(dq)):
        if dq.popleft()<dq[j]:
            list1.append(len(dq)-2)

        
    
    
    
list1=[]
list1=list(map(int,s.readline().split()))
for i in range(len(list1),0,-1):
    dq.append(list1[i])
lazor(dq)