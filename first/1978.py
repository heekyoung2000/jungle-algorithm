#에라토스테네스의 체
n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
list2=[]
 
if n==1 and list1[0]==1:
    list1.remove(1)
else:
    for i in range(2,list1[n-1]+1):
        for j in list1:
            if j==1:
                list2.append(1)
            elif j%i==0 and j!=i:
                list2.append(j)
            else:
                continue
for i in list2:
    if i in list1:
        list1.remove(i)
print(len(list1))



#1만 있을 경우 0개
#인덱스 범위 초과 에러
#반복문안에서 list 삭제할 경우 원하는 값이 안나올 수 있음 예를 들어 1 4 일때 output:1 answer:0 오류

        