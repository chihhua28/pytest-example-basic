from typing import Dict, Union

def update_value_by_key(origin_dict:Dict, key: str, value: Union[str, int, float]) -> Dict:

    if key not in origin_dict:
        raise KeyError
    
    new_dict = origin_dict
    new_dict[key] = value
    return new_dict

def check_key_exists(dictionary: Dict, key: str) -> bool:
    
    if key in dictionary:
        return True
    else:
        return False