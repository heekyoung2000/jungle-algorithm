from sys import stdin as s
s=open("input.txt",'rt')

n,b=map(int,s.readline().split())#n,b를 입력받는다 n:행렬의 크기 , b:제곱수
list1=[list(map(int,s.readline().split())) for _ in range(n)]
#2차원 배열 이용해서 list로 받기

def mul(U,list2):
    print(U,list2)
    n=len(U)
    answer = [[0]*n for _ in range(n)] #빈 2차원 배열 선언
    for row in range(n): #행렬 풀때 3개의 반복문을 이용해서 품
        for col in range(n):
            result=0
            for i in range(n): #기존의 list2를 곱한다. 이때 list2는 배열 list1과 같다.
                result+= U[row][i]*list2[i][col]
            answer[row][col]=result%1000
    print(answer)
    return answer

def pow(list1,b):
    if b==1:
        for x in range(len(list1)):
            for y in range(len(list1)):
                list1[x][y]%=1000
        return list1
    

    tmp = pow(list1,b//2)
    if b%2!=0:
        return mul(mul(tmp,tmp),list1)
    else:
        return mul(tmp,tmp)
    
    
for i in pow(list1,b):
    print(*i) #포인터로 이용해서 출력하기