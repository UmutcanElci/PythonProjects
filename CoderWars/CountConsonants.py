def consonant_count(s):
    count = len([i for i in s if  i.lower() not in "aeiou" and i.isalpha()])
    return count
    