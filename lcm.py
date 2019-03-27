def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)



a = input("")
b = input("")

result = gcd(a,b)

print a*b/result
