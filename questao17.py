def verify(string):
    number = False
    letter = False

    for i in string:

        if i.isalpha():
            letter = True

        if i.isdigit():
            number = True

    return letter and number