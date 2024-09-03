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
        if stringNumber.startswith("//"):                                          # for custom delimiter
            numberWithDelim = stringNumber.split("//")[1]                          # "//;;;\n1;;;2|;;;3"  -> ["", ";;;\n1;;;2;;;3"]
            delim = numberWithDelim[:numberWithDelim.find("\n")]   
            stringNumber = numberWithDelim[numberWithDelim.find("\n")+1:] 

        stringNumber = stringNumber.replace("\n",delim)
        numbers = stringNumber.split(delim)
        negativeNumbers = []
        for number in numbers:
            if int(number) < 0:
                negativeNumbers.append(int(number))
            result += int(number)
        
        if len(negativeNumbers) != 0:
            commaSeparatedNegativeValue = ", ".join(map(str, negativeNumbers))
            print("negatives not allowed:",commaSeparatedNegativeValue)
            raise ValueError("negatives not allowed.")
        print("result:{}".format(int(result)))
        return int(result)
