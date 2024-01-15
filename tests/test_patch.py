import pytest
from unittest.mock import patch

import src.add

# define substitute function
def substitute_func(num1, num2):
    return("Successfully patched!")
        
def test_add_num(monkeypatch):
    monkeypatch.setattr(src.add,"add_num", substitute_func)  
    result = src.add.add_num(1,3)
    assert result == "Successfully patched!"

# method one: use pytest monkeypatch
def test_add_num(monkeypatch):
    monkeypatch.setattr(src.add, "add_num", substitute_func) 
    result = src.add.add_num(1,3) # it has to be src.add.add_num() instead of add_num()
    assert result == "Successfully patched!"

# method two: use pytest monkeypatch and with statements
def test_add_num_with_monkeypatch(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr("src.add.add_num", substitute_func)   
        assert src.add.add_num(2,3)== "patch successfully!"

# method three: use pytest monkeypatch by defining the mock function in the test function
def test_add_num_with_monkeypatch(monkeypatch):
    def mock_add_num(num1, num2):
        return "patch successfully!"
    monkeypatch.setattr("src.add.add_num", mock_add_num)
    result = src.add.add_num(2, 3)
    assert result == "patch successfully!"
    

# method four: use pytest mark parametrize and unittest.mark patch
@pytest.mark.parametrize("num1, num2, fake_result", [
    (2, 3, 10),  
    (5, 7, 12),  
])
@patch("src.add.add_num")
def test_add_num_with_patch(mock_add_num, num1, num2, fake_result):
    
    mock_add_num.return_value = fake_result
    result = src.add.add_num(num1, num2)
    assert result == fake_result
    mock_add_num.assert_called_once_with(num1, num2)
        
