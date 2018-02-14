def genPrimes():
    a = 2
    primes = []
    primes.append(a)
    condition = True
    while a<10:
        for element in primes:
            condition1 = (a % element) != 0
            condition = condition1 & condition
            
        if condition == True:
            primes.append(a)
            yield a
        print(a)
        a += 1