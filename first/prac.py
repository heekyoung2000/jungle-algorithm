'''from typing import MutableSequence
import bisect

def bubble_sort(a:MutableSequence)->None:
    n=len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]

#개선된 버블 정렬- 교환된 횟수에 따라 중단 방식 적용
def bubble_sort(a:MutableSequence) -> None:
    n=len(a)
    for i in range(n-1):
        exchng = 0
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                exchng+=1
        if exchng == 0:
            break
        
        
#개선된 버블정렬 - 이미 정렬된 원소를 제외한 나머지만 비교
def bubble_sort(a:MutableSequence)-> None:
    n=len(a)
    k=0
    while k < n-1:
        last = n-1
        for j in range(n-1,k,-1):
            if a[j-1] > a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                last=j
        k= last
        
#셰이커 정렬 - 맨뒤에서 맨앞으로 스캔했다가 다시 뒤로 스캔
def shaker_sort(a:MutableSequence) -> None:
    left = 0
    right = len(a)-1
    last= right
    while left < right:
        for j in range(right,left,-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j],a[j-1]
                last=j
        left = last
        
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                last = j
        right = last
        
#단순 삽입 정렬 알고리즘
def insertion_sort(a:MutableSequence)->None:
    n=len(a)
    for i in range(1,n):
        j=i
        tmp = a[i]
        while j>0 and a[j-1]>tmp:
            a[j]==a[j-1]
            j-=1
        a[j]=tmp 
        
#이진 삽입 정렬 알고리즘
def binary_insertion_sort(a:MutableSequence)->None:
    n=len(a)
    for i in range(1,n):
        key=a[i]
        pl = 0
        pr = i-1
        
        while True:
            pc = (pl + pr) //2
            if a[pc]==key:
                break
            elif a[pc]<key:
                pl = pc+1
            else:
                pr=pc-1
            if pl >pr:
                break
        pd = pc +1 if pl <= pr else pr+1
        
        for j in range(1,pd,-1):
            a[j] = a[j-1]
        a[pd]=key
        
def binary_insertion_sort(a:MutableSequence)->None:
    for i in range(1,len(a)):
        bisect.insort(a,a.pop(i),0,i)
        
#셸 정렬
def shell_sort(a:MutableSequence)-> None:
    n = len(a)
    h= n//2
    while h>0:
        for i in range(h,n):
            j=i-h
            tmp = a[i]
            while j>=0 and a[j]>tmp:
                a[j+h]=a[j]
                j-=h
            a[j+h]=tmp
        h//=2
        
# 퀵 정렬- 퀵정렬 중 하나만 적용
def insertion_sort():
    for i in range(left+1,right+1):
        j=1
        tmp=a[i]
        while j>0 and a[j-1]>tmp:
            a[j]= a[j-i]
            j-=1
        a[j]=tmp
        
def qsort(a:MutableSequence,left:int, right:int)->None:
    if right - left <9:
        insertion_sort(a,left,right)
    else:
        pl = left
        pr = right
        m = sort3(a,pl,(pl+pr)//2,pr)
        x = a[m]
        
        a[m],a[pr-1] = a[pr -1],a[m]
        pl+=1
        pr -=2
        while pl<=pr:
            while a[pl]<x:pl +=1
            while a[pr]> x:pr -=1
            if pl <=pr:
                a[pl],a[pr] = a[pr],a[pl]
                pl +=1
                pr -= 1
                
        if left < pr : qsort(a,left,pr)
        if pl < right : qsort(a,pl,right)


#재귀 호출 예시
#팩토리얼
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)'''
    
    
def q_sort(list1,left,right):
    pl=left
    pr=right
    x = list1[(left+right)//2]
    
    while pl<=pr:
        while list1[pl]<x:
            pl+=1
        while list1[pr]>x:
            pr-=1
        if pl<=pr:
            list1[pl],list1[pr]=list1[pr],list1[pl]
            pl+=1
            pr-=1
        
        if left<pr:
            q_sort(list1,left,pr)
        if pl < right:
            q_sort(list1,pl,right)
    
list1=[3,1,2,5,3,1]
q_sort(list1,0,len(list1)-1)
print(list1)
