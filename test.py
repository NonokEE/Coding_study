def condition(a, b):    
    if abs(a) < abs(b):
        return 1
    elif abs(a) == abs(b):
        if a < b:
            return 1
        else:
            return 0
    else: 
        return 0

print(condition(-1, 1))