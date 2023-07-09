def sum_digits(number):
    number = abs(number)
    strNum = str(number)
    sum = 0
    for i in strNum:
        sum += int(i)
    return sum     
    