from sys import stdin as s
from collections import deque

s=open("input.txt",'rt')
n=int(s.readline())
dq=deque()
'''result=[]
idx=0
cnt=0

    
def stack(list1):
    global result
    global idx
    global cnt
    
    for i in range(len(list1)):
        dq.append(i)
    first_idx=(-1)
    while len(dq)>1 and first_idx> -len(dq):
        #print(dq,first_idx)
        if list1[dq.pop()] < list1[dq[first_idx]]:
            idx=dq[first_idx]+1
            #print(list1[dq[-1]])
            result.append(idx)
            first_idx=(-1)
        else:
            first_idx-=1
            dq.append(idx-1)
    
    if len(list1)==1:
        result.append(1)
    else:
        for _ in range(len(list1)-len(result)):
            result.append(0)
    
        
    return reversed(result)  


list1=list(map(int,s.readline().split()))

for s in stack(list1):
    print(s,end=" ")''' #답은 나오는데 시간초과
    
result=[]
answer=[0]*n
def stack(list1):
    for i in range(len(list1)):
        while result:
            if list1[result[-1][0]] < list1[i]:
                result.pop()
            else:
                answer[i]=(result[-1][0]+1)
                break
        result.append((i,list1[i]))    

list1=list(map(int,s.readline().split()))
stack(list1)
print(* answer)