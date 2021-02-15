from firsttoolbox.guessnumber import get_random_number

def test_type_output():
    number=get_random_number()
    assert type(number)==int
