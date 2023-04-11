import math
def find(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return True
    return False    
                
t= int(input())

max_list=[]
for i in range(t):
    n=int(input())
    max_list.append(n)
    
for n in max_list:
    num_list=[]
    for i in range(2,n//2+1):
        if find(i)==False and find(n-i)==False:
            num_list.append(i)
    result= max(num_list)
    print(f'{result} {n-result}')            

##1. 시간초과 문제
##2. num_list 초기화 안해줌
        
    