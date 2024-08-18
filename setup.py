from setuptools import find_packages, setup
from typing import List

# Constant for editable install
HYDRA_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]
            if HYDRA_E_DOT in requirements:
                requirements.remove(HYDRA_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. No requirements will be installed.")
    
    print("Requirements loaded:", requirements)  # Debug print statement
    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Ashwin',
    author_email='ashwingunasekaran1999@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
