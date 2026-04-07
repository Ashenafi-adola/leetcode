n = int(input())
for i in range(n):
    s = input()
    rt = ''
    for j in range(len(s)-1, -1, -1):
        if s[j] == 'p':
            rt += 'q'
        elif s[j] == 'q':
            rt += 'p'
        else:
            rt += s[j]
    print(rt)