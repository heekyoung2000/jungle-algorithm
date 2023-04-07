T=int(input())
for i in range(T):
    list1 = list(input().split())
    num=int(list1[0])
    for j in list1[1]:
        print(j*num,end='')
    print()