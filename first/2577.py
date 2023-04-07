a=int(input())
b=int(input())
c=int(input())
result = a*b*c
list1 = list(map(int, str(result)))

for i in range(10):
    print(list1.count(i),end="\n")

#숫자 입력 받을떄 줄바꿈으로 입력받는 방법 알아보기