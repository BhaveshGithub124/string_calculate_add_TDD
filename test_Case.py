from add_calculator import addCalulator

def test_emptyString():
    result = addCalulator("")
    assert (result == 0)

def test_single_number_in_string():
    string = "1"
    assert (addCalulator(string) == 1)

