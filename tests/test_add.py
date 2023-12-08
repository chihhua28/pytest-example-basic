from src.add import add_num
from src.add import add_str
import pytest

@pytest.mark.num_test
def test_add_num():
    assert add_num(3,4) == 7

@pytest.mark.str_test
def test_add_str():
    str1 = 'Hello'
    str2 = 'World'
    assert add_str(str1, str2) == "HelloWorld"

@pytest.mark.str_test
def test_add_str_failed():
    str1 = 12
    str2 = 13
    with pytest.raises(TypeError):
        add_str(str1, str2)