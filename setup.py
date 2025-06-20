from setuptools import setup,find_packages
from typing import List

HYPEN_DOT_E = '- e.'
def get_requirements(file_path:str)->List[str]:
    """
    read and install requirements text file
    """
    with open('requirements.txt') as file:
        requirements = file.readlines()
        requirements = [req.replace(" ",'\n') for req in requirements]


    if  HYPEN_DOT_E  in requirements:
        requirements.remove(HYPEN_DOT_E)

setup(
   name = 'Music recommandation system',
   author= 'sankar',
   author_email='narayanansankar480@gmail.com',
   version= '0.0.0.1',
   packages= find_packages(),
   install_requires = get_requirements('requirements.txt')
)