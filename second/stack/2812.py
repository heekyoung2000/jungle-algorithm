from sys import stdin as s
from collections import deque

#걍 틀림
'''list1=[]
result_list=[]


n,k=map(int,s.readline().split())
num=list(map(str,s.readline()))
print(num)

for i in num:
    i=int(i)
    list1.append(i)
list1.sort()
print(list1)
number=list1[:-1-k:-1]
for j in number:
    result_list.append(str(j))
result=''.join(result_list)
print(result)'''

s=open("input.txt","rt")
stack =[]
n,k = map(int,s.readline().split())
numbers=s.readline().rstrip()


for num in numbers:
    while stack and k>0 and stack[-1]<num:#stack이 있고 k가 0보다 크고 마지막으로 남은 수가 num보다 작을때
        stack.pop() #최근 스택 삭제
        k-=1 #새로운 스택에 넣어줄 것이므로 주어진 갯수에서  하나 뺌
    stack.append(num) #stack에 숫자 넣음

if k>0:
    print(''.join(stack[:-k])) #만약 k가 0보다 크고 스택에 주어진 숫자보다 더 많이 남아있다면 제한 갯수만큼 출력하기
else:
    print(''.join(stack)) #제한 갯수인 k에 맞췄으므로 stack에 join