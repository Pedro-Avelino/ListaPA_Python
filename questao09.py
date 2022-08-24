def string_calc(id1):
    for n in id1:
        print(n)
        if n.isdigit():
            amount = amount + int(n)
            average = average * int(n)
    print("A soma foi: ", amount)
    print("A média foi: ", average)