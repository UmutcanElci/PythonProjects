def high_and_low(numbers):
    number_lst = [int(a) for a in numbers.split()]
    return str(max(number_lst)) + " " + str(min(number_lst))

