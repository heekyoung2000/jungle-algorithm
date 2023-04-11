#자리수가 1,2일 떄 모두 등차수열
'''1.99까지는 무조건 등차수열이므로 99보다 작으면 입력한 수 출력
2.99보다 큰 수 일경우 cnt를 99로 설정하고 각 자리 수의 차를 구하고 각 자리수가 같으면 cnt 1씩 증가'''
n=int(input())

if n<100:
    print(n)
else:
    cnt=99
    for i in range(99,n+1):
        a=i//100
        b=i%100//10
        c=i%10
        first = b-a
        second = c-b
        if first==second:
            cnt+=1
        else:
            continue
    print(cnt)    
        
    