from sum_func import add, add_positive
# Tests
def test_add_positive_2_and_3():   
    assert add_positive(2, 3) == 5

def test_add_negative_5_and_positive_10():
    assert add_positive(-5, 10) == None

def test_type_check():
    assert type(add_positive(2,3))==int 

def test_add_positive_10_and_negative_5():
    assert add_positive(10, -5) == None

def test_add_positive_0_and_0():
    assert add_positive(0, 0) == None

def test_add_0_and_0():
    assert add(0, 0) == 0

def test_add_2_and_3():
    assert add(2,3) == 5