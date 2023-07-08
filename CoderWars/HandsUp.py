def get_positions(n):
    h1 = n % 3
    h2 = (n // 3)%3
    h3 = (n // 9) %3 
    
    return h1,h2,h3
        