def converter(list, dictionary):
    for x in list:
        if x not in dictionary:
            list.remove(x)