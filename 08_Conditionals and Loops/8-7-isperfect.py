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

def prime_split(num):
    if num <= 0:
        return []

    result = []
    n = int(num ** 0.5) 

    while n > 1:
        tmp = divmod(num, n)
        if tmp[1] == 0:
            if isprime(n):
                result.append(n)
            else:
                result += prime_split(n)

            if isprime(tmp[0]):
                result.append(tmp[0])
            else:
                result += prime_split(tmp[0])

            break
        else:
            n -= 1
    return sorted(result)

def isperfect(num):
    factors = prime_split(num)
    factors.insert(0, 1)
    return sum(factors) == num

while True:
    num = int(raw_input('input a number: '))
    print isperfect(num)