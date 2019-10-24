#!/usr/bin/env python

from setuptools import setup, find_packages

from src import python_exercise

version = ".".join(map(str, python_exercise.__version__))

setup(
    name='python_exercise',
    version=version,
    description='Simple python project for recruitment',
    maintainer='https://github.com/ModusCreateOrg',
    license='MIT', 
    url='https://github.com/ModusCreateOrg/python-exercise',
    author="Alejandro Castillo",
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
    ],
    entry_points={
        'console_script': [
            'python_exercise = python_exercise.__main__:main'
        ]
    }
)
