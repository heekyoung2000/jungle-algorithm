from sys import stdin as s
from collections import deque
import re
s=open("input.txt","rt")
#-가 있으면 그 앞에 가로 넣고 다음 -나 끝이 날때까지 합하기
from collections import deque

list1=s.readline().strip()
number= re.split('([^0-9])',list1)


# def bfs(start):
#     sum=0
#     while start<len(number) and number[start]!='-':
#         if number[start]=='+':
#             start+=1
#         else:
#             sum+=int(number[start])    
#             start+=1
#     return sum
# result=0
# for i in range(1,len(number)):
#     if number[i]=='-':  
#         a=bfs(i+1)
#         if a>int(number[i-1]):
#             result+=int(number[i-1])-a
#         else:
#             result+=a-int(number[i-1])

# for i in range(len(number)):
#     if '-' not in number:
#         if number[i]=='+':
#             continue
#         else:
#             result+=int(number[i])
# print(result)

#-로 나누기
arr = input().split('-') #입력받은 문자열을 -로 나누기
s=0
print(arr)
for i in arr[0].split('+'): #처음에 분리한 문자열을 계산
    print(i)
    s+=int(i)
for i in arr[1:]: #분배법칙을 활용한 것으로 뒤에 있는 나머지 값들은 모두 - 해줌
    for j in i.split('+'):
        print(j)
        s-=int(j)

print(s)

#아니 왜 s.readline()은 split이 안되냐


