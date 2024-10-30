def gcd(a , b):
    while b:
        a, b = b, a % b
        return a
    a, b, c, d = map(int, input())
    x = a * d
    y = b * c
    z = gcd(x, y)
