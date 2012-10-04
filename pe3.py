num = 600851475143

def uoc_nguyen_to(n):
    li = []

    while n > 1:
        i = 3
        while n % i != 0:
            i = i + 2
        li.append(i)
        n = n / i
    return li

print max(uoc_nguyen_to(num))
print uoc_nguyen_to(num)
