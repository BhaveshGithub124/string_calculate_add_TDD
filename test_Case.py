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