from sys import stdin as s
from collections import deque

s=open("input.txt","rt")

n,k= map(int,s.readline().split())
list1=list(map(str,s.readline()))


dq=deque()
dq_max=deque()

for i in list1:
    dq.append(int(i))
    


while len(dq)<=n and len(dq)!=0:
    if len(dq_max)==0:
        dq_max.append(dq.pop())
    else:
        if dq_max[-1]<dq[-1]:
            dq_max.append(dq.pop())
        elif dq_max[-1]>dq[-1]:
            dq_max.appendleft(dq.pop())


for i in range(n-k):
    print(dq_max.pop(),end="")
    
