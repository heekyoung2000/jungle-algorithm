import sys

def check(new_number,cnt,n):
    while True:
        if new_number!=n:
            cnt+=1
            a=new_number//10
            b=new_number%10  
            c=(a+b)
            if c>=10:
                c=(a+b)%10
            else:
                c=(a+b)
            new_number = 10*b+c
        else:
            return cnt
        

n=int(sys.stdin.readline())
a=n//10
b=n%10
c=(a+b)
cnt=1
if c>=10:
    c=(a+b)%10
else:
    c=(a+b)
new_number = 10*b+c
print(check(new_number,cnt,n))

        
    

    
    
