from sys import stdin as s
from collections import deque

s=open("input.txt",'rt')
n=int(s.readline())
dq=deque()

def stack(list1):
    result=[0]*n
    for i in range(len(list1)):
        while dq:
            if list1[dq[-1]]<list1[i]:
                dq.pop()
            else:
                result[i]=dq[-1]+1
                break
        dq.append(i)
    return result  


list1=list(map(int,s.readline().split()))
for i in stack(list1):
    print(i,end=" ")
    
result=[]
answer=[0]*n # 통신 할 수 없는 경우에 0을 출력해야 하므로 선언할 때 부터 0으로 구성된 배열로 선언
def stack(list1):
    for i in range(len(list1)):
        print(result, answer)
        while result:
            if list1[result[-1]] < list1[i]: #현재 값보다 뒤에 있는 값이 더 크면 통신할 수 없으므로 pop실행
                result.pop()
            else: #그 외에는 통신이 가능하므로 현재 인덱스에 1을 더한 값을 answer에 저장한다.
                answer[i]=(result[-1]+1)
                break
        result.append(i) #result에 인덱스와 list의 값을 모두 저장한다.   

list1=list(map(int,s.readline().split()))
stack(list1)
#print(* answer) #포인터를 사용한 것으로 해당하는 인덱스 주소값을 출력
for i in answer:
    print(i,end=" ")