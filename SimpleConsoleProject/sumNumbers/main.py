def sum_numbers(*nums):
    sum = 0
    for numbers in nums:
        sum += numbers
    
    return sum


print(sum_numbers(10,34,66,2))