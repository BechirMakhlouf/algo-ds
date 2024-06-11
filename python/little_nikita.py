t = int(input())

for _ in range(t):
    n, m = input().split()
    if m > n:
        print("no")
        continue
    if (int(n) - int(m)) % 2 != 0:
        print("no")
        continue
    print("yes")
