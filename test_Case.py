from add_calculator import addCalculator

def test_emptyString():
    result = addCalculator("")
    assert (result == 0)

def test_single_number_in_string():
    string = "2"
    assert (addCalculator(string) == 2)

