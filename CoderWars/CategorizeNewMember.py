def open_or_senior(data):
    return ["Senior" if a >= 55 and b > 7 else "Open" for a,b in data]