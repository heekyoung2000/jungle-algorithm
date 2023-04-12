#random 함수 쓰면 확률적으로 나오는 값이므로 시간이 오래 걸릴 수 있어서 사용하지 않음

'''import sys

def ran(sum,list1):
    new_sum=0  
    for i in range(1,n):
        d = abs(list1[i]-list1[i-1])
        new_sum+=d
    
    while True:
        
        if new_sum>sum:
            sum=new_sum
            ran(sum,list1)
            break
        elif new_sum==sum:
            print(new_sum)
            break
        else:
            ran(sum,list1)
            break
            
def _sort(list1):
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            list1[j-1],list1[j]=list1[j],list1[j-1]
            print(list1)

        
    


n=int(sys.stdin.readline())
list1=list(map(int,sys.stdin.readline().split()))
new_list=[]
sum=0
for i in range(1,n):
        d = abs(list1[i]-list1[i-1])
        sum+=d
_sort(list1)   
print(sum)
ran(sum,list1)
'''
import sys

#재귀
n=int(sys.stdin.readline())
list1=list(map(int,sys.stdin.readline().split()))
visited=[False]*n
arr=[]
answer = float('-inf')

def sol(depth):
    global answer
    if depth == n:
        total=0
        for i in range(n-1):
            total +=abs(list1[i]-list1[i+1])
        answer=max(answer,total)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            sol(depth+1)
            visited[i]=False
            arr.pop()
            
sol(0)
print(answer)





#순열
import sys
from itertools import permutations

n=int(sys.stdin.readline())
graph = list(map(int,sys.stdin.readline().split()))
max_ans = float("-inf")
for i in permutations(graph):
    ans=0
    for j in range(n-1):
        ans+=abs(i[j]-i[j+1])
    max_ans = max(max_ans,ans)
    
print(max_ans)

    