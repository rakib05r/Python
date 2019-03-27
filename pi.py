import random as r
import math as m


inside = 0

total = 1000

for i in range(0, total):

    x2 = r.random()**2
    y2 = r.random()**2

    print x2,"    ",y2

    if m.sqrt(x2 + y2) < 1.0:
        inside += 1


pi = (float(inside) / total) * 4


print(pi)
