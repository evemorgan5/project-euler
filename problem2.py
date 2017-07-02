def Fn(n):
    fib = ((1 / (5 ** 0.5) * ((1 + 5 ** 0.5) / 2) ** n) -
    	(1 / (5 ** 0.5) * ((1 - 5 ** 0.5) / 2) ** n))
    return int(round(fib, 0))

n = 2
total = 0
while Fn(n) < 4000000:
	if Fn(n) % 2 == 0:
		total += Fn(n)
	n += 1

print total
