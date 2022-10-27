a = [input(), input(), input()]
s = ''.join(a)

if len(s) > 20 and s.isalpha():
    mx = a[0] if len(a[1]) < len(a[0]) > len(a[2]) else a[1] if len(a[0]) < len(a[1]) > len(a[2]) else a[2]
    n