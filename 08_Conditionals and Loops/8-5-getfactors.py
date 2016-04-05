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

while True:
    num = int(raw_input('input a number: '))
    print getfactors(num)