def gcd(num1, num2):
    while num2 > 0:
        tmp = num1 % num2
        num1 = num2
        num2 = tmp
    return num1

def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)

print gcd(24, 18)
print lcm(24,18)
