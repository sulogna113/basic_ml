#It helps in building your application as a package so that other project can use this in their project.
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirments=[]
    with open(file_path) as f:
        requirments=f.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    
    return requirments

setup(
    #mets data about the project
    name='mlproject',
    version = '0.0.1',
    author = 'Sulogna',
    packages=find_packages(),
    install_requires= get_requirments('requirments.txt')
)