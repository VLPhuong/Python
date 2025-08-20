import math

def nguyento(n):
    if n < 2: return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dem(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    K = dem(N)
    if nguyento(K):
        print('YES')
    else:
        print('NO')