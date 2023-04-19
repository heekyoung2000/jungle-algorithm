#공유기 설치
# 중복 순열 
from sys import stdin as s

s=open("input.txt","rt")
n,m = map(int,s.readline().split())
list1=[]

for i in range(n):
    number=int(s.readline())
    list1.append(number)
list1.sort()#주어진 정렬 오름차순으로 정렬(이분탐색의 기본 조건)


start = 1#공유기의 최소 거리
end = list1[-1]-list1[0]# 최대 거리
result=0
while ( start <=end ):
    mid = (start+end)//2 #최소거리와 최대거리의 중간값을 구함
    cur = list1[0] #처음 값으로 지정
    cnt=1
    for i in range(1,len(list1)):
        if list1[i] >= cur+mid: #앞에서 부터 설치 
            cur = list1[i]
            cnt+=1
    if cnt>=m: #m개의 이상의 공유기를 설치할 수 있을 경우 거리를 증가
        start = mid+1 
        result=mid
    else: end= mid-1 #m개의 이상 공유기를 설치할 수 없는 경우 거리를 감소
            
print(result)


'''start = 1
end = list1[-1]-list1[0]
result=0
while(start<=end):
    mid = (start+end)//2
    cur = list1[0]
    cnt=1
    for i in range(1,len(list1)):
        if list1[i] >= cur+mid:
            cur = list1[i]
            cnt+=1
    if cnt >=m:
        start = mid+1
        result =mid
    else:
        end=mid-1

print(result)'''
    

start =1
end = list1[-1]-list1[0]
while( start <=end ):
    mid = (start+end)//2
    cur = list1[0]
    cnt=1
    for i in range(1,len(list1)):
        if list1[i] >= cur+mid:
            cur = list1[i]
            cnt+=1
    if cnt>=m:
        start = mid+1
        result=mid
    else:
        end=mid-1
print(result)
    

