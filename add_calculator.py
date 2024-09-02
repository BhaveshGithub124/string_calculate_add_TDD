def addCalculator(stringNumber):
    printString = stringNumber.replace("\n","\\n")
    print('\nTest string:"{}"'.format(printString))

    if len(stringNumber) == 0:
        print("result:0")
        return 0
    elif len(stringNumber) == 1:
        print("result:{}".format(int(stringNumber)))
        return int(stringNumber)
    else:
        result = 0
        delim = ","
        if stringNumber[0] == "/": # for custom delimiter
            delim = stringNumber[2] #delimiter position is at index 2 for custom delimiter
            stringNumber = stringNumber[4:] #numbers start from index 4 for custom delimiter

        stringNumber = stringNumber.replace("\n",delim)
        numbers = stringNumber.split(delim)
        for number in numbers:
            result += int(number)
        print("result:{}".format(int(result)))
        return int(result)
