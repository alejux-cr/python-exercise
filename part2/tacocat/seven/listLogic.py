
from itertools import combinations

def split_str_by(p_string, p_separator=','):
    try:
        new_list = p_string.split(p_separator)
        int_list = str_list_to_int_list(new_list)
        return int_list
    except ValueError:
        return []

def str_list_to_int_list(p_str_list):
    try:
        int_list = list(map(int, p_str_list))
        return int_list
    except ValueError as verr:
        return []
    except Exception as ex:
        return []

def generate_set_pair_sum7(p_string,p_separator=','):
    result_list = []
    tuple_list = split_str_by(p_string, p_separator)
    if len(tuple_list) > 0:
        combs = combinations(tuple_list, 2)
        
        for pair_tuple in combs:
            if (pair_tuple[0]+pair_tuple[1]) == 7:
                result_list.append(pair_tuple)
        
        if len(result_list) == 0:
            result_list.append('No set sums up to 7')
    
    return result_list
