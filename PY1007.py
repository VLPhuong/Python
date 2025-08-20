t = int(input())
for _ in range(t):
    N, X, M = map(float, input().split())
    years = 0
    while N < M:
        N *= (1 + X / 100)
        years += 1
    print(years)