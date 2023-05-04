#괄호 해결
from sys import stdin as s
from collections import deque
s=open("input.txt","rt")

# list1=s.readline().strip()

# sum=0
# arr= list1.split('-')
# for i in arr[0].split('+'):
#     sum+=int(i)
# for j in arr[1:]:
#     for z in j.split('+'):
#         sum-=int(z)
    
# print(sum)

#가장 긴 부분 수열찾기
n=int(s.readline())
arr=list(map(int,s.readline().split()))
print(arr)

DP=[1]*(n+1)

for i in range(0,n):
    for j in range(0,i):
        if arr[i] >arr[j]:
            DP[i]=max(DP[i],DP[j]+1) #누적합 배열
            
            
print(max(DP))
