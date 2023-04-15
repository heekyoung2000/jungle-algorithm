#배열로 나열했을때 맨 마지막에 추가된 수보다 크면 기준 수를 큰 수로 바꾼다.
#그 후 다음 배열의 수가 크면 cnt+=1
#중복 제외

#sudo code
#list에 저장
#리스트를 거꾸로 돌면서 m에 마지막 수 저장
#그 전 인덱스 값이 같으면 cnt+=1 외에는 i-=1
#그 전 인덱스 값이 클 경우 cnt+=1 i-=1해주고 m에 인덱스 값 저장
#게속 비교

from sys import stdin as s

def result(list1):
    cnt=1
    m=list1[-1]
    for i in range(n-1,0,-1):
        if m<list1[i-1]:
            m=list1[i-1]
            cnt+=1
    return cnt
    

s=open('input.txt','rt')
n = int(s.readline())
list1=[]
for i in range(n):
    num=int(s.readline())
    list1.append(num)


print(result(list1))


