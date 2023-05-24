from sum_func import add, add_positive
# Tests
def test_add_positive():
    assert add_positive(2, 3) == 5
    assert add_positive(-5, 10) == None
    assert add_positive(0, 0) == None
    assert type(add_positive(2,3))==int