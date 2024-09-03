import pytest
from add_calculator import addCalculator

def test_emptyString():
    result = addCalculator("")
    assert (result == 0)

def test_single_number_in_string():
    string = "2"
    assert (addCalculator(string) == 2)

def test_two_number_in_string_with_comma_delimiter():
    string = "19,20"
    assert (addCalculator(string) == 39)

def test_three_number_in_string_with_comma_delimiter():
    string = "10,20,30"
    assert (addCalculator(string) == 60)

def test_four_number_in_string_with_comma_delimiter():
    string = "0,50,100,150"
    assert (addCalculator(string) == 300)

def test_unlimited_number_in_string_with_comma_delimiter():
    string = "0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500"
    assert (addCalculator(string) == 1995)

def test_handle_new_line_in_string():
    string = "1\n2,3\n4,5"
    assert (addCalculator(string) == 15)

def test_handle_custom_delimiter():
    string = "//#\n4#5#6"
    assert (addCalculator(string) == 15)

    string = "//|\n1|2|3"
    assert (addCalculator(string) == 6)

    string = "//;\n10;20"
    assert (addCalculator(string) == 30)

    string = "//@\n10@20@30@40"
    assert (addCalculator(string) == 100)

    string = "//*\n2*4*6*8*10"
    assert (addCalculator(string) == 30)

    string = "//-\n2-4-6"
    assert (addCalculator(string) == 12)

def test_negative_number():
    string = "-1,2,-3,4"
    with pytest.raises(ValueError) as exceptionInfo:
        reuslt = addCalculator(string)
    assert str(exceptionInfo.value) == "negatives not allowed."

    stringWithCustomDelimNegativeNum = "//*\n2*4*-6*-8*10"
    with pytest.raises(ValueError) as exceptionInfo:
        addCalculator(stringWithCustomDelimNegativeNum)
    assert str(exceptionInfo.value) == "negatives not allowed."

def test_ignore_numbers_greater_than_1000():
    string = "//#\n4#5#6#1001"
    assert (addCalculator(string) == 15)

    string = "//-\n2-4-6-1010-8-1200"
    assert (addCalculator(string) == 20)

    string = "//|\n1|2|3|1000|4"
    assert (addCalculator(string) == 1010)

    string = "//*\n2*4*6*8*10*999"
    assert (addCalculator(string) == 1029)

def test_custom_delim_with_variable_length():
    string = "//[---]\n2---4---6---1010---8---1200"
    assert (addCalculator(string) == 20)

    string = "//[***]\n2***4***6***1010***8***1200***10"
    assert (addCalculator(string) == 30)

    stringWithCustomDelimNegativeNum = "//[####]\n1####4####-6####-8####10####-11####-12####13"
    with pytest.raises(ValueError) as exceptionInfo:
        addCalculator(stringWithCustomDelimNegativeNum)
    assert str(exceptionInfo.value) == "negatives not allowed."

    string = "//[.....]\n2.....3.....4.....5.....6.....100.....200"
    assert (addCalculator(string) == 320)

def test_custom_delimiter_having_more_than_one_type():
    string = "//[;][#]\n4#5;6;1001#10"
    assert (addCalculator(string) == 25)