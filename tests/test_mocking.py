from unittest.mock import MagicMock

def test_mocking_method():
    mock_object = MagicMock()
    mock_object.some_method.return_value = 42
    
    result = mock_object.some_method()
    
    assert result == 42