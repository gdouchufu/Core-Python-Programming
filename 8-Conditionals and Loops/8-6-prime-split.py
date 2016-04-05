def isprime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
        
    n = int(num ** 0.5)
    while n > 1:
        if num % n == 0:
            return False
        else:
            n -= 1
    else:
        return True

def getfactors(num):
    if num <= 0:
        return []

    result = set([])
    n = int(num ** 0.5)
    while n > 0:
        tmp = divmod(num, n)
        if tmp[1] == 0:
            result.add(n)
            result.add(tmp[0])
        n -= 1

    return sorted([x for x in result])

def prime_split(num):
    if num <= 1:
        return []
    if isprime(num):
        return [num]

    factors = getfactors(num)
    if len(factors) > 2:
        result = []
        maxF = factors[-2]
        tmp = divmod(num, maxF)

        result += prime_split(maxF)
        result += prime_split(tmp[0])

        return sorted(result)
    else:
        return []
    
while True:
    num = int(raw_input('input a number: '))
    print prime_split(num)