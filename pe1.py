#-------------------------------------------------
li=[]
for i in range(1,1000):
    if i%3==0 or i%5 ==0:
        li.append(i)
              
print sum(li)
#____________________________________________________
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print result

# Best
print sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])
#______________________________________________________
x = 0
for i in range(0,1000,3):
	x = x + i
for i in range(0,1000,5):
	x = x + i
for i in range(0,1000,15):
	x = x - i
print x
#---------------------------------------

