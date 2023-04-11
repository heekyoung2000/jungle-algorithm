#퀵정렬로 풀어보기
'''def quick_sort(list1,left,right):
    pl=left #왼쪽 커서
    pr=right #오른쪽 커서
    x=list1[(left+right)//2] # 여기서 오류 남 원래는 (left+right)//2=x로 설정
    
    while pl<=pr:
        while list1[pl] < x:
            pl+=1 # pivot보다 작은 수 일경우 오른쪽으로 한칸 이동
        while list1[pr] > x:
            pr-=1 #pivot보다 큰 수 일경우 왼쪽으로 한칸 이동
        if pl<=pr:
            list1[pl],list1[pr]=list1[pr],list1[pl]
            pl+=1
            pr-=1
    if left < pr:
        quick_sort(list1,left,pr)
    if pl < right:
        quick_sort(list1,pl,right)            
            
    
n= int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)
quick_sort(list1,0,len(list1)-1)
for j in list1:
    print(j)'''
## 1. 시간초과 -> 퀵정렬의 경우 최악의 조합인 o(n*2)이 나올수 있으므로 합병 정렬로 풀어야함


#병합정렬 -> 시간초과 -> 왜...?
'''def merge_sort(list1,left,right):
    if left < right:
        center = (left+right)//2
        
        merge_sort(list1,left,center)
        merge_sort(list1,center+1, right)
        
        p=j=0
        i=k=left
        
        while i<=center:
            buff[p]=list1[i]
            p+=1
            i+=1
            
        while i<=right and j<p:
            if buff[j] <= list1[i]:
                list1[k]=buff[j]
                j+=1
            else:
                list1[k]=list1[i]
                i+=1
            k+=1
            
        while j<p:
            list1[k]=buff[j]
            k+=1
            j+=1
        
        
        
n= int(input())
list1=[]
buff=[0]*n
for i in range(n):
    number=int(input())
    list1.append(number)

merge_sort(list1,0,n-1)
for i in list1:
    print(i)'''
    

#pypy3가 아니라 python으로 써서 그런지는 모르겠지만 자꾸 시간초과 남...
import sys
    
def sort(list1):
    if len(list1)<2:
        return list1
    mid = len(list1)//2
    left = sort(list1[:mid])
    right = sort(list1[mid:])
    
    return merge(left,right)

def merge(left,right):
    a=0 #left
    b=0#right
    new_list=[]
    while a<len(left) and b<len(right):
        if left[a]<right[b]:
            new_list.append(left[a])
            a+=1
        elif left[a]>right[b]:
            new_list.append(right[b])
            b+=1
    while a<len(left):
        new_list.append(left[a])
        a+=1
    while b<len(right):
        new_list.append(right[b])
        b+=1  
    return new_list
    
n = int(sys.stdin.readline())
list1=[]
for i in range(n):
    number= int(input())
    list1.append(number)
for j in sort(list1):
    print(j)

        
            