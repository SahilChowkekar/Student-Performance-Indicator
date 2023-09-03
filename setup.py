from setuptools import find_packages,setup
from typing import List



HYPE_E_DOT="_e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != '-e .']

        

    return requirements

setup(
name = 'ml-porject',
version = '0.0.1',
author = 'Sahil',
author_email = 'chowkekar9@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)




