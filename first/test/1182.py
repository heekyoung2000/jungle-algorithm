#나중에 내가 기억할 수 있을까..?

import sys
n,s = map(int,sys.stdin.readline().split())
list1=list(map(int,sys.stdin.readline().split()))


cnt=0
def dfs(idx,result):
    global cnt
    if sum(result)==s and len(result)!=0:
        cnt+=1
    
    for i in range(idx,n):
        result.append(list1[i])
        dfs(i+1,result)
        result.pop()
            
dfs(0,[])
print(cnt)