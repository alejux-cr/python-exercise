
import json
from cfn_flip import flip, to_yaml, to_json
from cfn_tools import load_yaml, dump_json, load_json
from cfn_clean import clean
import os
import sys

ROOT_DIR = os.path.dirname(__file__)

def is_project_name_palindrome(p_name):
    reversed_name = p_name[::-1]
    if p_name == reversed_name:
        return True
    else:
        return False


def yaml_to_json(p_input_file):
    json_out = ROOT_DIR+'/../../../tacocat_cf.json'

    with open( p_input_file,'r') as yaml_in:
        yaml_data = load_yaml(yaml_in)
        yaml_data = clean(yaml_data)

    with  open(json_out,'w') as out_file:
        json_data = dump_json(yaml_data)
        json_data = load_json(json_data)     
        json.dump(json_data ,out_file, sort_keys=True, indent=4, separators=(',', ': '))
        print('*--*--*--*--*--*--*--*--*--*--*--*--**--*--*--*--*--*--*--*--*--*--*--*')
        print('The new JSON file has been created in the root folder of the project with the name tacocat_cf.json')
        print('*--*--*--*--*--*--*--*--*--*--*--*--**--*--*--*--*--*--*--*--*--*--*--*')



    


    