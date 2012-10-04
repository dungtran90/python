fib = [1,2]; x = 0; total = 2
while fib[x] < 4000000:
	x = len(fib)
	fib.append(fib[x-2] + fib[x-1])
	if fib[x] % 2 == 0:
		total += fib[x]
print total