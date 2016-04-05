def factorial(N): # N! = 1*2*3...*N
    if N <= 0:
        return None
    return reduce(lambda x,y:x*y, range(1,N+1))

while True:
    num = int(raw_input('input a number: '))
    print factorial(num)