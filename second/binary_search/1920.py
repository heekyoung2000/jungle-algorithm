# 이진탐색은 정렬이 필수
# 각 lista를 이진탐색하고 listm은 한개씩 target으로 지정한다.
from sys import stdin as s
from collections import deque

result=0

'''def exist(lista,listm,start,end):
    global result
    lista=sorted(lista)
    for i in listm:
        target=i
        print(target)
        while start<=end:
            result=0
            mid=(start+end)//2
            if lista[mid]==target:
                result+=1
                break
            elif lista[mid]<target:
                return exist(lista,listm,start,end-1)
            else:
                end= mid-1
        if result==0:
            print(0)
        else:
            print(1)'''
            
def binary_search(lista,target,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    if target==lista[mid]: #target을 lista[mid]와 비교 lista[mid]==target은 lista[mid]를 target에 비교하는 것이므로 오류
        return 1
    elif target > lista[mid]:
        return binary_search(lista,target,mid+1,end)
    else:
        return binary_search(lista,target,start,mid-1)


s=open("input.txt","rt")
n=int(s.readline())
lista= sorted(list(map(int,s.readline().split())))
m=int(s.readline())
listm = list(map(int,s.readline().split()))
for i in listm:
    print(binary_search(lista,i,0,n-1))

#중복 때문에 시간초과 남...
# 이진탐색은 정렬이 필수
# 각 배열을 
'''import sys

def exist(lista,listm):
    set(lista)
    for i in listm:
        if i in lista:
            print(1)
        else:
            print(0)
        
    


#s=open("input.txt","rt")
n=int(sys.stdin.readline())
lista= set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
listm = list(map(int,sys.stdin.readline().split()))
exist(lista,listm)'''
