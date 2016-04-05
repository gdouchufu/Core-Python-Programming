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

while True:
    num = int(raw_input('input a number: '))
    print isprime(num)