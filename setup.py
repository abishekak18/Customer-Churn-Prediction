from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip() and not req.strip().startswith('#')]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Abishek E',
    author_email='abiabishek2004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
