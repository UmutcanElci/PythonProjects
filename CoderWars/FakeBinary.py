def fake_bin(x):
    line = ""
    for element in x:
            if int(element)<5:
             line += "0"
            else:
                line += "1"
                
    return line