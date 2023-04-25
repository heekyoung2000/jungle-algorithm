from sys import stdin as s
from collections import deque

s=open("input.txt","rt")
n,m = map(int,s.readline().split())
list1=list(map(int,s.readline().split()))
list1.sort()

#접근 방법 - 이진 탐색을 통해 나무의 높이를 설정하기
def binary_search(start,end):
    while start<=end:
        #start, end 설정
        mid = (start+end)//2 #mid를 설정해줌
        sum=0
        for i in range(n):
            cut=list1[i]-mid #mid와 list의 차이를 구함
            if cut>=0:
                sum+= cut #sum에 저장
            else:
                sum+=0 #cut값이 0보다 작다면 0을 더해줌
        if sum>m: #만약 sum이 m보다 크면 sum을 줄여야 하므로 mid를 크게 설정해야함 따라서 start를 mid+1로 설정
            start=mid+1
        elif sum==m: #만약 sum==m이면 바로 mid로 출력
            print(mid)
            break
        else:
            end=mid-1 #만약 sum이 m보다 작으면 end=mid-1을 수행
    if sum!=m and sum>m: #만약 sum==m이 아니고 sum이 m보다 크면 mid는 m과 가장 가까운 수니까 mid 출력
        print(mid)
    elif sum!=m and sum<m: #만약 sum==m이 아니고 sum이 m보다 작으면 mid-1을 수행(m은 항상 sum보다 커야 하므로)
        print(mid-1)
     
binary_search(0,max(list1))       
    