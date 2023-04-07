a,b = map(str, input().split())
r_a=''.join(list(reversed(a)))
r_b=''.join(list(reversed(b)))
if int(r_a)>int(r_b):
    print(r_a)
else:
    print(r_b)
