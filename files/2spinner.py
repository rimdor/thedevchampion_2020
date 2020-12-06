def carousel_crypt(s):
    i = 0
    f = ''
    for c in s:
        f += bin(ord(c)).zfill(7)[2:][i:] + bin(ord(c)).zfill(7)[2:][:i]
        i = (i + 1) % 8
    return int(f, 2)

pwd = input('Password please\n')

if carousel_crypt(pwd) == 6838670745825122932886199347866255930502612544243548566773595:
    print('Welcome master <3')
else:
    print('Go away')