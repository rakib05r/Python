u = []

def test(p):
    
    printf()
    
    if u[0]<=p:
        return 1
    else:
        return 0


def printf():
    m=16;
    a=5.0;
    c=3.0;
    z=7.0;

    for num in range (1,21):
        r=(a*z+c)%m;
        #print r;
        z=r;
        u.append(z/m)
        #print z/m;
        #print r,z/m ;



    
p = input("")
a = test(p)

print u
print a

