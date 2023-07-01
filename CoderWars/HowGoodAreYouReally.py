def better_than_average(class_points, your_points):
    # Your code here
    classTotal = sum(class_points) / len(class_points)
    
    if classTotal > your_points:
        return False
    else:
        return True
    
        
        
        
    
    