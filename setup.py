from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
    

setup(
    name = "Sensor-Fault-Detection",
    version= "0.0.1",
    author= "Tiyyagura Chandra Reddy",
    author_email= "tchandrareddy21@gmail.com",
    install_requires = get_requirements('requirements.txt'),
    packages= find_packages()
)