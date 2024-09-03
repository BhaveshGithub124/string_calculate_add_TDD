import re
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
        originalString = stringNumber
        if stringNumber.startswith("//"):                                          # for custom delimiter
            numberWithDelim = stringNumber.split("//")[1]                          # "//;\n1;2;3"  -> ["", ";\n1;2;3"]
            delim = numberWithDelim[0]
            stringNumber = numberWithDelim[numberWithDelim.find("\n")+1:]

            startIdxForVarLenDelim = numberWithDelim.find("[")
            if startIdxForVarLenDelim != -1:
                stringNumber,delim = multiple_and_variable_len_delim(originalString.split("\n")[0], stringNumber)

        stringNumber = stringNumber.replace("\n",delim)
        numbers = stringNumber.split(delim)
        negativeNumbers = []
        for number in numbers:
            if int(number) < 0:
                negativeNumbers.append(int(number))
            elif int(number) > 1000:
                continue
            result += int(number)
        
        if len(negativeNumbers) != 0:
            commaSeparatedNegativeValue = ", ".join(map(str, negativeNumbers))
            print("negatives not allowed:",commaSeparatedNegativeValue)
            raise ValueError("negatives not allowed.")
        print("result:{}".format(int(result)))
        return int(result)
    
def multiple_and_variable_len_delim(numberWithDelim, stringNumber):
    patterns = r'\[(.*?)\]'
    delimiters = re.findall(patterns, numberWithDelim)
    escaped_delimiters = [re.escape(delim) for delim in delimiters]
    pattern = '|'.join(escaped_delimiters)
    stringWithCommaDelim = re.sub(pattern, ",",stringNumber)
    return stringWithCommaDelim, ","
    
    
