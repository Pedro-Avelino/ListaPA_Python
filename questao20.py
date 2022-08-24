def intsec_sets(x, y):    
    x = {10, 20, 30, 40, 50, 60}
    y = {20, 40, 60}
    z = x.difference(y)
    x = z
    
    print(x)