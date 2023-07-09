def growing_plant(up_speed,down_speed,desired_height):
    day = 0
    height = 0
    if desired_height == 0:
        return 1
    while height < desired_height:
        day += 1
        height += up_speed
        
        if height >= desired_height:
            break
        
        height -= down_speed
        
    return day
    