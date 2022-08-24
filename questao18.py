def number_list(l1, l2, l3):
    for id1 in l1:
        if (id1 % 2 != 0):
            l3.append(id1)
            if len(l3) != 0:
                break
    
    for id2 in l2:
        if not (id2 % 2 != 0) :
            l3.append(id2)
    
    print(l3)