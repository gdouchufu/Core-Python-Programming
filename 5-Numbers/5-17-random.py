import random

def rand_sort_num():
    res = []
    N = random.randint(1, 100)
    while N > 0:
        n = random.randint(0, 2**31-1)
        res.append(n)
        N -= 1

    res.sort()
    return res

print rand_sort_num()

