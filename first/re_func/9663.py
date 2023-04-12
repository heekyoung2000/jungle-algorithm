# 순열-> 재귀함수 사용
import sys
n=int(sys.stdin.readline())
cnt=0

pos= [0]*n #각 열에 배치한 퀸의 위치
flag_a = [False]*n #각 행에 퀸을 배치했는지 체크
flag_b = [False]*(n*2-1) #대각선 방향으로 퀸을 배치했는지 체크
flag_c = [False]*(n*2-1)  #대각선 방향으로 퀸을 배치했는지 체크
list1=[]

'''def put():
    for i in range(n):
        print(f'{pos[i]:2}',end='')
    print()'''
    
    
def set(i):
    for j in range(n):
        cnt=0
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+(n-1)]:
            pos[i]=j
            if i==n-1:
                #put()
                cnt+=1
                list1.append(cnt)
            else:
                flag_a[j]= flag_b[i+j] = flag_c[i-j+(n-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)]=False


set(0)
print(sum(list1))
            