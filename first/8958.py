import sys
n=int(input())
for i in range(n):
    num,sum=0,0
    list1= list(sys.stdin.readline())
    for i in list1:
        if i=="O":
            num+=1
            sum+=num
        else:
            num=0
    print(sum)

        
        