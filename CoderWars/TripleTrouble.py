def triple_trouble(one, two, three):
    #your code here
    new = ""
    length = len(one)
    for i in range(length):
        if i < len(one):
            new += one[i]
        if i < len(two):
            new += two[i]
        if i < len(three):
            new += three[i]
    return new

#Or use join function 