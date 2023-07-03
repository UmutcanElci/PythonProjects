def pipe_fix(nums):
    minPipe = min(nums)
    maxPipe = max(nums)
    lst = []
    
    for x in range(minPipe,maxPipe+1):
        lst.append(x)
    return lst
    