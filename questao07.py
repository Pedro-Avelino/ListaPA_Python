def compare(id1, id2):
    test = True
    for aux in id1:
        if aux in id2:
            continue
        else:
            test = False
    return test