def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        total = 0  
        for num in numbers: 
            total += num
        avg = total / len(numbers)
        return avg
    
print(find_average([1,2,3]))
