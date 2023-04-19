from sys import stdin as s
#만약 이전 항이 지금 항보다 작으면 부분수열 가능 but 작으면 불가능
#시간 복잡도 O(N**2)
s=open("input.txt",'rt')


def dp(list1,n):
    result=[1]*n
    for i in range(0,n):
        for j in range(0,i):
            if list1[i]>list1[j]:
                result[i] = max(result[i],result[j]+1)
    #print(result)
    print(max(result))

n=int(s.readline())
list1=list(map(int,s.readline().split()))
dp(list1,n)

#이진탐색을 통해 시간 복잡도 줄임 O(Nlogn)
n=int(s.readline())
list1=list(map(int,s.readline().split()))



