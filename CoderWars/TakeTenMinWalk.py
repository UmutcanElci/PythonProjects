def is_valid_walk(walk):
    n = 0
    s = 0
    e = 0
    w = 0

    if len(walk) == 10:
        n = walk.count('n')
        s = walk.count('s')
        e = walk.count('e')
        w = walk.count('w')
        if n - s == 0 and e - w == 0:
            return True
        else:
            return False
    else:
        return False
