import src.add

def substitute_func(num1, num2):
    return("Successfully patched!")
        
def test_add_num(monkeypatch):
    monkeypatch.setattr(src.add,"add_num", substitute_func)  
    result = src.add.add_num(1,3)
    assert result == "Successfully patched!"
