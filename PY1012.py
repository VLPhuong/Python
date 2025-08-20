a, K, N = map(int, input().split())

if (N-a) <= 0:
    print(-1)
else:
    r = (-a) % K              
    start = r if r != 0 else K 
    if start > limit:
        print(-1)
    else:
        b = start
        while b <= limit:
            print(b, end=" ")
            b += K