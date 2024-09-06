from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        reruirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for rep in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Palak',
author_email='vanpariyapalak@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)