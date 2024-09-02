from add_calculator import addCalculator

def test_emptyString():
    result = addCalculator("")
    assert (result == 0)

def test_single_number_in_string():
    string = "2"
    assert (addCalculator(string) == 2)

def test_two_number_in_string_with_comma_delimiter():
    string = "1,2"
    assert (addCalculator(string) == 3)