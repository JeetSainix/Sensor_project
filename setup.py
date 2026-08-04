from setuptools import find_packages,setup
from typing import List
hypen_e_dot='-e.'
def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace('\n','') for req in requirement]
        if hypen_e_dot in requirement:
            requirement.remove(hypen_e_dot)
        return requirement
setup(
    name='fault detection',
    version='0.0.1',
    author='Jeet',
    author_email='abc@gmail.com',
    install_requirement=get_requirement('requirement.txt'),
    packages=find_packages()
)
