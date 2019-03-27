u = []
count = []
m = 16
a = 5
c = 3
z = 7

for num in range (m):
    r = (a*z+c)%m
    z = r
    u.append(float(z)/m)

print u
def test(w):
    count = 0

    for i in w:
        print u[0] ," ",i
        if u[0]<=i:
            count+=1
        else:
            break
    
    return count


p = []
f = input("")
for i in range(f):
    j = input("")
    p.append( float(j))

l = len(p)


c = test(p)


print c,"  ",l

print float(c)/float(l)







