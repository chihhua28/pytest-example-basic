def add_num(num1: int, num2: int):
    result = num1 + num2
    return result

def add_str(str1: str, str2: str):
    if not(isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError('Wrong type')
    else:
        return str1 + str2