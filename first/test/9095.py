'''import sys

cnt=0
number=[]

def fibo(num):
    if num==1:
        return 1
    if num==2:
        return 2
    if num==3:
        return 4
    
    return fibo(num-3)+fibo(num-2)+fibo(num-1)
           
    

T=int(sys.stdin.readline())
result=[]
for i in range(T):
    num=int(sys.stdin.readline())
    result.append(num)'''
#Top-down 방식
'''import sys
cnt=0
def s(num):
    global cnt
    if num<0:
        return 0
    if num==0:
        return 1
    cnt=0
    for i in range(1,4):
        cnt+=s(num-i)
    return cnt
    
t=int(sys.stdin.readline())
result=[]
for i in range(t):
    num=int(sys.stdin.readline())
    result.append(s(num))

for j in result:
    print(j)'''
    
import sys

def plus(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    
    return plus(n-3)+ plus(n-2)+ plus(n-1)

    
    
T=int(sys.stdin.readline())
result=[]
for i in range(T):
    n=int(sys.stdin.readline())
    result.append(plus(n))
for j in result:
    print(j)       
    
    
    
    