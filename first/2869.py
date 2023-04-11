a,b,v = map(int,input().split())

#v-b : 올라가야할 거리
#a-b : 하루에 갈수 있는 거리 = a-b
res=(v-b)//(a-b)

if(v-b)%(a-b)!=0:
    print(res+1)
else:
    print(res)
        
'''import sys
a,b,v=map(int,sys.stdin.readline().split())

if a>=v: 
    cnt=1
elif a-b==1:
    cnt=v-a+1
else:
    up=a-b
    if (v-a)%up==0:
        cnt=(v-a)//up
    else:
        cnt=v//up+1
print(cnt)'''