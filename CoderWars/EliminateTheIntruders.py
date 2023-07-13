def eliminate_unset_bits(number):
    number = number.replace('0', '') 
    if number == '':
        return 0
    a = int(number, 2) 
    return a

    
    