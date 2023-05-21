n = int(input())
for i in range(n):
    a = input().upper()
    b = input()
    for ch in b:
        if ch not in a:
            print('NO')
            break
    else:
        print('YES')