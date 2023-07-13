def round_and_round(n,a,b):
    result = (a+b) % n
    if result == 0:
        result = n
        
    return result
    