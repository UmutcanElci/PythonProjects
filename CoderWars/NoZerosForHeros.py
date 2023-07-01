def no_boring_zeros(n):
    if n == 0:
        return n
    a = str(n).rstrip('0')
    return int(a)