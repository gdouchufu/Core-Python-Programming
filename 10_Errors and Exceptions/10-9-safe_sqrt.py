import math, cmath
  
def safe_sqrt(num):
    try:
        result = math.sqrt(num)
    except ValueError:
        result = cmath.sqrt(num)
    return result
  
if __name__ == '__main__':  
    print safe_sqrt(123)
    print safe_sqrt(-123)