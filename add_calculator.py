def addCalculator(stringNumber):
    print('\nTest string:"{}"'.format(stringNumber))
    if stringNumber == "":
        print("result:0")
        return 0
    print("result:{}".format(int(stringNumber)))
    return int(stringNumber)