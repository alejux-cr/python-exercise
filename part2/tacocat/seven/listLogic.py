
from itertools import permutations

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
        return [0]
    except Exception as ex:
        return [0]

def generate_set_pair_sum7(p_list):
    print('work in progress...')