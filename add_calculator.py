def addCalculator(stringNumber):
    print('\nTest string:"{}"'.format(stringNumber))

    if len(stringNumber) == 0:
        print("result:0")
        return 0
    elif len(stringNumber) == 1:
        print("result:{}".format(int(stringNumber)))
        return int(stringNumber)
    else:
        result = 0
        stringNumber = stringNumber.replace("\n",",")
        numbers = stringNumber.split(",")
        for number in numbers:
            result += int(number)
        print("result:{}".format(int(result)))
        return int(result)
