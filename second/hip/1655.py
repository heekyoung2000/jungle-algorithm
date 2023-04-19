from sys import stdin as s
from heapq import heapify
import heapq
    
#이 방법은 안돼고 2개의 힙을 설정해줘야 함    


s=open("input.txt",'rt')
n=int(s.readline())
hq=[]

'''def sorting(hq):
    for i in range(1,len(hq)):
        c=i
        while c!=0:
            r=(c-1)//2
            if hq[r]< hq[c]:
                hq[r],hq[c] = hq[c],hq[r]
            
    
for i in range(n):
    num=int(s.readline())
    heapq.heappush(hq,num)
    print(hq)
    if len(hq)%2!=0:
        #정렬해야함
        #sorting(hq)
        
        mid=len(hq)//2
        print(hq[mid])
    else:
        mid2=len(hq)//2
        if hq[mid2-1]>hq[mid2]:
            print(hq[mid2])
        else:
            print(hq[mid2-1])'''


'''leftheap=[]
rightheap=[]
answer=[]
for i in range(n):
    num= int(s.readline())
    
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,(-num,num))
    else:
        heapq.heappush(rightheap,(num,num))
    if rightheap and leftheap[0][1]>rightheap[0][0]:
        min=heapq.heappop(rightheap)[0]
        max=heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap,(-min,min))
        heapq.heappush(rightheap,(max,max))
        
    answer.append(leftheap[0][1])
print(leftheap,rightheap)
for j in answer:
    print(j)'''
    
    
leftheap=[]
rightheap=[]
result=[]

for i in range(n):
    num=int(s.readline())
    
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,(-num,num))
    else:
        heapq.heappush(rightheap,(num,num))
    if rightheap and leftheap[0][1]>rightheap[0][0]:
        min=heapq.heappop(rightheap)[0]
        max= heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap,(-min,min))
        heapq.heappush(rightheap,(max,max))
    
    result.append(leftheap[0][1])
    
for i in result:
    print(i)