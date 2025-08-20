s = input()

upper_count = sum(1 for c in s if c.isupper())
lower_count = sum(1 for c in s if c.islower())


if lower_count >= upper_count:
    kq = s.lower()
else:
    kq = s.upper()

print(kq)