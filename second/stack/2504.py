#먼저 괄호열을 입력받아 list에 저장한다.
#1. 괄호열이 올바른지 판단
#1-1 만약 괄호열이 맞다면 값으로 계산하는 함수로 이동
#1-2 만약 괄호열이 틀리다면 0으로 출력
#2.값으로 계산하는 함수
#2-1 ()==2로 지정,[]==3으로 지정
#2-2 다른 괄호가 나올때마다 곱해주는데 만약 짝이 맞는 괄호를 만나면
# 현재 곱하고 더해두었던 누적 합을 res에 저장한다. 짝맞는 닫힌 괄호에 맞춰서 temp를 2또는 3으로 나누어 준다. 



from sys import stdin as s
from collections import deque

dq=deque()

'''def correct(n):
    #단순하게 () 짝이 맞지 않으면 0을 리턴 아니면 다른 함수로 이동
    cnt=0
    for i in range(len(n)):
        if n[i]=="(":
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                break
          
    if cnt==0:
        result(n)
    else:
        print(0)'''
    
def result(n):
    res=0
    temp=1
    
    for i in range(len(n)):
        if n[i]=='(': #( 와 [일 경우 dq에 추가하고 temp에 각각 2또는 3을 곱해줌
            dq.append(n[i])
            temp*=2
        elif n[i]=='[':
            dq.append(n[i])
            temp*=3
        elif n[i]==']': # ]일 경우 1) 이전 항이 [일 경우 짝이므로 res에 temp값을 저장한다 2)만약 (이거나 dq가 False 이면 res=0으로 반환하고 반복문 종료
            if n[i-1]=='[':
                res+=temp
                
            if not dq or dq[-1]=='(':
                res=0
                break
            
            temp=temp//3 #temp값은 ]를 없앴으므로 3으로 나눠준다. 그 후 dq의 최신 값([)을 빼준다.
            dq.pop()
    
        elif n[i]==')':
            if n[i-1]=='(':
                res+=temp
                
            if not dq or dq[-1]=='[':
                res=0
                break
            
            temp=temp//2 #위의 방법과 같지만 )이므로 2로 나눠준다.
            dq.pop()
            
    if len(dq)!=0: #만약 모든 과정을 다 했는데도 dq 값이 남아 있다면 res=0으로 출력
        res=0
                
    print(res)        
            
            

s=open('input.txt','rt')
n =list(map(str,s.readline().strip()))
result(n)



