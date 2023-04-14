import sys
#달팽이는 올라가고 시프다

'''a,b,v = map(int,sys.stdin.readline().split())

if a==v:
    print(1)
elif (v-b)%(a-b)==0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)'''

#소수 찾기
'''import math
def is_prime(x):
    if x==1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
    return True

n=int(input())
cnt=0
list1=list(map(int,input().split()))
for j in list1:
    if is_prime(j) is True:
        cnt+=1
print(cnt)'''

#골드바흐의 추측
'''import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


T=int(sys.stdin.readline())
list1=[]
for i in range(T):
    n=int(sys.stdin.readline())
    list1.append(n)
for j in list1:
    result=[]
    for i in range(2,j//2+1):
        if is_prime(i) is True and is_prime(j-i) is True:
            result.append(i)
    m=max(result)
    print(f'{m} {j-m}')'''


#한수
#세자리 수 이상부터 각 자리 수의 차이가 같아야지 됨

'''x=int(input())
if x>99:
    cnt=99
    for i in range(100,x+1):
        a=i//100
        b=i%100//10
        c=i%10
        if (b-a)==(c-b):
            cnt+=1
else:
    cnt=x
print(cnt)'''
    
#종이 자르기

#팩토리얼
'''def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
    
n=int(input())
print(fac(n))'''

#하노이탑 no : 옮겨야 할 원반의 개수 x : 시작 기둥의 번호, y: 목표 기둥의 번호
'''하노이탑(원판, "시작기둥"에서 "대상기둥"으로 '보조기둥"을 활용해서):

cnt=0
def hanoi(n,x,y):
    global cnt
    if n>1:
        hanoi(n-1,x,6-x-y)
    print(f'{x} {y}')
    if n>1:
        hanoi(n-1,6-x-y,y)
    
n=int(sys.stdin.readline())
print(2**n-1)
if n<=20:
    
    hanoi(n,1,3)
'''

#n-queen
'''import sys
n=int(sys.stdin.readline())

pos=[0]*n
check_r =[False]*n
check_x =[False]*(n*2-1)
check_y =[False]*(n*2-1)
list1=[]

def set(i):
    for j in range(n):
        cnt = 0
        if not check_r[j] and not check_x[i+j] and not check_y[i-j+(n-1)]:
            pos[i]=j
            if i==n-1:
                cnt+=1
                list1.append(cnt)
            else:
                check_r[j]=check_x[i+j]=check_y[i-j+(n-1)]=True
                set(i+1)
                check_r[j]=check_x[i+j]=check_y[i-j+(n-1)]=False




set(0)
print(sum(list1))'''

#z문제 r=행,c=열
'''dict=[[0,0],[1,0],[0,1],[1,1]]

n,r,c=map(int,sys.stdin.readline().split())
ans = 0
while n!=0:
    n-=1
    if r<2**n and c<2**n:
        ans+= (2**n) *0
        
    elif r>=2**n and c<2**n:
        ans+=(2**n)*(2**n)*2
        r-=2**n
    elif r<2**n and c>=2**n:
        ans+=(2**n)*(2**n)*1
        c-=2**n
    else:
        ans+=(2**n)*(2**n)*3
        r-=2**n
        c-=2**n
        
print(ans) '''

#퀵정렬
def quick_sort(list1,left,right):
    pl=left
    pr=right
    x=list1[(left+right)//2]
    
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
        quick_sort(list1,left,pr)
    if pl < right:
        quick_sort(list1,pl,right)
            

n=int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)
quick_sort(list1,0,len(list1)-1)
for j in list1:
    print(j)
    
def quick_sort(list1,left,right):
    pl=left
    pr=right
    pivot=list1[(left+right)//2]
    
    while pl<=pr:
        while list1[pl]<pivot:
            pl+=1
        while list1[pr]>pivot:
            pr-=1
        if pl <=pr:
            list1[pl],list1[pr]=list1[pr],list1[pl]
            pl+=1
            pr-=1
    if left < pr:
        quick_sort(list1,left,pr)
    if pl < right:
        quick_sort(list1,pl,right)
        
n=int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)
quick_sort(list1,0,len(list1-1))
for j in list1:
    print(j)
    
#합병 정렬
def sort(list1):
    if len(list1)<2:
        return list1
    mid=len(list1)//2
    left=sort(list1[:mid])
    right = sort(list1[mid:])
    
    return merge(left,right)

def merge(left,right):
    a=0
    b=0
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
    
n=int(sys.stdin.readline())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)
for j in sort(list1):
    print(j)

