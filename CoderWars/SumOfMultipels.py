def sum_mul(n, m):
    if n > 0 and m > 0:
        total = 0
        for i in range(n,m,n):
            total += i
        return total
    else:
        return "INVALID"
    
    
    """
    def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID
    """
    