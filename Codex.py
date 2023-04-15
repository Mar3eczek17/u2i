# Python 3

def mult_numbers(a, b):
    return a * b


# Unit test
def test_mult_numbers():
    assert mult_numbers(3, 4) == 12
    assert mult_numbers(0, 10) == 0
    assert mult_numbers(4, 0) == 0


# Unit test
def test_mult_numbers_negative():
    assert mult_numbers(-1, 10) == -10
    assert mult_numbers(10, -1) == -10
