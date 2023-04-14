from sys import stdin as s
s=open('input.txt','rt')
n,m = map(int,s.readline().split())

result =[]
def dfs():
    if len(result)!=0 and len(result)==m:
        print(' '.join(map(str,result)))
        return 
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()