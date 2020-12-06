def f1(s):
    return s[::-1]

def f2(s):
    return s[::2]+ s[1::2]

def f3(s):
    r = ''
    for c in s:
        r += chr(ord(c) ^ 0xf)
    return r

def f4(s):
    r = ''
    for c in s:
        r += chr(ord(c) - 1 if ord(c) != 32 else 126)
    return r

def f5(s):
    r = ''
    for c in s:
        r += chr(ord(c) + 1 if ord(c) != 126 else 32)
    return r

def f6(s):
    r = ''
    idx = 1
    for i in range(30):
        idx *= 11
        idx %= 31
        r += s[idx-1]
    return r

def f7(s):
    return s.swapcase()

def f8(s):
    r = ''
    for c in s:
        if 'a'<=c<='z':
            r += chr((ord(c)-ord('a') + 13)%26 + ord('a'))
        else:
            r += c
    return r

def f9(s):
    r = ''
    for c in s:
        if 'A'<=c<='Z':
            r += chr((ord(c)-ord('A') + 13)%26 + ord('A'))
        else:
            r += c
    return r

def f10(s):
    return s[-1] + s[:-1]

def check(s):
    if len(s)!= 30 or 'XHFS%~p8#j:&ih<jim~NYFj5i!oEX%' != f6(f6(f2(f1(f7(f10(f5(f5(f6(f7(f6(f8(f2(f9(f8(f6(f5(f6(f2(f6(f7(f3(f3(f5(f2(f2(f2(f8(f2(f1(f10(f4(f8(f5(f5(f8(f2(f9(f2(f5(f3(f7(f8(f3(f4(f5(f10(f4(f1(f9(s)))))))))))))))))))))))))))))))))))))))))))))))))):
        print('Nope')
    else:
        print('OK!')

check(input('Enter the flag: '))
