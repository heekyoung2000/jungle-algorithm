from sys import stdin as s
from collections import deque

s=open('input.txt','rt')
n,k = map(int,s.readline().split())

dq=deque()
list1=[]

for i in range(1,n+1):
    dq.append(i)

while len(dq)>0:
    for j in range(k-1):
        dq.append(dq.popleft())
    a=dq.popleft()
    list1.append(a)
print(f'<',end="")
for i in range(len(list1)-1):
    print(list1[i],end=", ")
print(list1[-1],end=">") 
 
#다시 품
dq=deque()
list1=[]

for i in range(1,n+1):
    dq.append(i)
    
while len(dq)>0:
    for j in range(k-1):
        dq.append(dq.popleft())
    a=dq.popleft()
    list1.append(a)
print(f'<',end="")
for i in range(len(list1)-1):
    print(list1[i],end=", ")
print(list1[-1],end=">")

