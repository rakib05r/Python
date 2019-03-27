u = []


def test(w):
    count = 0
    l = len(w)
    print w
    print l

    for i in range(1,l):
        if u[0]<=p:
            count+=1;
    
    return count

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


p = raw_input("")
#p = ".375 .1 .2 .3 .4 .5 .6 .7 .8 .9"

p = p.split()

l = len(p)



printf()
c = test(p)

print c,"  ",l

print float(c)/float(l)







