import os
import subprocess
from functionalities import is_project_name_palindrome
from pathlib import Path


def create_django_project(p_proj_name='tacocat'):

    if is_project_name_palindrome(p_proj_name):
        proj_dir_name = './'+p_proj_name+'/'

        virtual_env_path_python = Path('./env/Scripts/', 'python.exe')
        virtual_env_path_pip = Path('./env/Scripts/', 'pip.exe')
        virtual_env_path_django = Path('./env/Scripts/', 'django-admin.exe')
        project_path_start = Path('./tacocat/', 'manage.py')
        project_path_req = Path('./tacocat/', 'requirements.txt')
        proj_freeze = Path('freeze', '>')
        project_path_readme = Path('./tacocat/', 'README.md')

        p1 = subprocess.run(['pip','install','virtualenv'], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        if p1.returncode != 0:
            print(p1.stderr)
            print('This tool has some minimum requirements installed: Python 3 and pip. Please check with python -v or pip -v.')
            print('To install the requirements go to:')
            print('https://www.python.org/downloads/')
            return

        p2 = subprocess.run(['virtualenv','env'], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        if p2.returncode != 0:
            print(p2.stderr)

        print('Virtual environment created at /env')       
        p3 = subprocess.run([str(virtual_env_path_pip),'install','django'], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        if p3.returncode != 0:
            print(p3.stderr)

        p4 = subprocess.run([str(virtual_env_path_pip),'install','djangorestframework'], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        if p4.returncode != 0:
            print(p4.stderr)

        p5 = subprocess.run([str(virtual_env_path_django),'startproject',p_proj_name], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        if p5.returncode != 0:
            print(p5.stderr)

        p6 = subprocess.run([str(virtual_env_path_pip),['freeze','>'],str(project_path_req)], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        if p6.returncode != 0:
            print(p6.stderr)

        print('** requirements.txt file created **')
        print('Starting the new Django project at localhost:8000  ..............')
        p7 = subprocess.run([str(virtual_env_path_python),str(project_path_start),'runserver',['127.0.0.1:8000','>>',str(project_path_readme)]], shell=True, stdout=subprocess.PIPE, text=True, check=True)
        print(p7.stdout)
        if p7.returncode != 0:
            print(p7.stderr)
        
        print('*--*--*--*--*--*--*--*--*--*--*--*--**--*--*--*--*--*--*--*--*--*--*--*')
        print('The new project has been created with a virtual environment(env folder).')
        print('For best practices activate running /env/Scripts/activate in the terminal.')
        print('*--*--*--*--*--*--*--*--*--*--*--*--**--*--*--*--*--*--*--*--*--*--*--*')

    else:
        print('The name you entered for the project is not a palindrome. [e.g. tacocat] Please try again or leave it empty and tacocat will be used as default.')
    


