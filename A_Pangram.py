n = int(input())
s = input().lower()
if n < 26:
    print("NO")
else:
    if len(set(list(s))) == 26:
        print("YES")
    else:
        print("NO")