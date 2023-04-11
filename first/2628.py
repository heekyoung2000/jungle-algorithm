
w,h=map(int,input().split())
cut_w=[0,h] 
cut_h=[0,w]
width=[]
height=[]
n=int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a==0:
        cut_w.append(b)
    else:
        cut_h.append(b)

cut_w.sort()
cut_h.sort()

for j in range(1,len(cut_h)):
    width.append(cut_h[j]-cut_h[j-1]) 
for i in range(1,len(cut_w)):
    height.append(cut_w[i]-cut_w[i-1]
)
print(max(width)*max(height))
