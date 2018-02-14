## ~/computerscience_intr/prime_numbers.py
## Returns prime numbers through a generator

def getPrimes():
    list_primes = []
    i=2
    while True:
        test = True
        for prime in list_primes:
            test = ((i % prime) != 0) & test
            if not test:
                break
        if test:
            yield i
            list_primes.append(i)
        i += 1