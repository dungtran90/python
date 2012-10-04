li=[]
for i in xrange(100,1000):
    for j in xrange(100,1000):
            t=i*j
            if str(t)== str(t)[::-1]:
                li.append(int(t))
                         
print max(li)

print max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])

print max([x*y for x in range(1,100) for y in range(1,100) if str(x*y)==str(x*y)[::-1]])

print max(x*y for x in range(1,100) for y in range(1,100) if str(x*y)==str(x*y)[::-1])

print ([x*y for x in range(1,10) for y in range(1,10) if x%5==0 and y%3==0])

