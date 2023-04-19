from sys import stdin as s
s=open("input.txt","rt")

#수찾기
'''def find(target):
    start=0
    end=n-1
    result=0
    while start<=end:
        mid=(start+end)//2
        if list1[mid]==target:
            result=1
            break
        elif list1[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return result
    
s=open("input.txt","rt")
n=int(s.readline())
list1=list(map(int,s.readline().split()))
list1.sort()

m=int(s.readline())
list2=list(map(int,s.readline().split()))

for i in list2:
    if find(i)==1:
        print(1)
    else:
        print(0)'''
        
dq=[]        
#최대 힙 

def heap(dq):
    dq.a
           

n =int(s.readline().split())
for i in range(n):
    number = int(s.readline())
    dq.append(number)
heap(dq)

