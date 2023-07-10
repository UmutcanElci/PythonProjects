
def square_digits(num):
    string = str(num)
    b =""
    for i in string:
        a = int(i) ** 2
        b += str(a)
    return int(b)
    # Your code here