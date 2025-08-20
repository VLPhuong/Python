k = int(input())
result = []

for _ in range(k):
    num = int(input())
    if num not in result:
        result.append(num)

print(*result)