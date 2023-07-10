import math

def is_square(n):
    if n < 0:
        return False
    return True if math.sqrt(n).is_integer() else False