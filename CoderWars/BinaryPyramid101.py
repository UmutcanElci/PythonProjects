def binary_pyramid(m,n):
    binSums = 0
    for x in range(m,n+1):
        binSums += int(bin(x)[2:])
    
    return str(bin(binSums)[2:])
    