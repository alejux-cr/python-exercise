#!/usr/bin/env python
import argparse
from functionalities import is_project_name_palindrome,yaml_to_json
from generate_django import create_django_project

l1 = "______ _                                                           _               _              _ "
l2 = "|  _  (_)                                                         | |             | |            | |"
l3 = "| | | |_  __ _ _ __   __ _  ___     __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __  | |_ ___   ___ | |"
l4 = "| | | | |/ _` | '_ \ / _` |/ _ \   / _` |/ _ | '_ \ / _ | '__/ _` | __/ _ \| '__| | __/ _ \ / _ \| |"
l5 = "| |/ /| | (_| | | | | (_| | (_) | | (_| |  __| | | |  __| | | (_| | || (_) | |    | || (_) | (_) | |"
l6 = "|___/ | |\__,_|_| |_|\__, |\___/   \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|     \__\___/ \___/|_|"
l7 = "     _/ |             __/ |         __/ |                                                           "
l8 = "    |__/             |___/         |___/                                                            "

def welcome():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)

def main():

    welcome()
    parser = argparse.ArgumentParser(description='This is our Django project generator tool set.',add_help=False)
    parser.add_argument('-h','--help', help='Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.',action='help',dest='help_command')
    parser.add_argument('-name',help='Project name. Must be a palindrome string [e.g. tacocat].', dest='project_name', type=str, required=False)
    parser.add_argument('-checkname',help='Check if the project name is a palindrome, returns True or False', dest='optional_name', type=str, required=False)
    parser.add_argument('-in',help='YAML input file. The selected file gets converted to a JSON file called tacocat_cf.json' ,dest='input_yaml', type=str, required=False)

    args = parser.parse_args()

    if(args.input_yaml):
        yaml_to_json(args.input_yaml)
    if(args.project_name):
        create_django_project(args.project_name)

if __name__ == '__main__':
    main()
