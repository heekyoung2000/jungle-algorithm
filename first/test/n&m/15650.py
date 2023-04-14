import sys
n,m=map(int,sys.stdin.readline().split())

s=[]
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):#오름차순
        if i not in s and (len(s)==0 or i > s[-1]):
            s.append(i)
            dfs()
            s.pop()

dfs()