def people_with_age_drink(age):
    line = " "
    if age <= 13:
        line = "drink toddy"
    elif 13 < age <=17:
        line = "drink coke"
    elif 17 < age <= 20:
        line = "drink beer"
    elif 20 < age:
        line = "drink whisky"
    return line