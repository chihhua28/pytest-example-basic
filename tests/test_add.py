from src.add import add_num
from src.add import add_str
import pytest

def test_add_num():
    assert add_num(3,4) == 7
    
@pytest.fixture(params=[(1,2),(3,4)])
def input_values(request):
    return request.param

def test_add_num(input_values):
    num1, num2 = input_values
    assert add_num(num1, num2) == num1 + num2

def test_add_str():
    str1 = 'Hello'
    str2 = 'World'
    assert add_str(str1, str2) == "HelloWorld"

def test_add_str_failed():
    str1 = 12
    str2 = 13
    with pytest.raises(TypeError):
        add_str(str1, str2)