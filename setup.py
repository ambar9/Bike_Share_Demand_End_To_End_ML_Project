from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:

    HYPEN_E_DOT = "-e ."
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name = "bike_share_demand",
    version= "0.0.1",
    description="This package is helps to predict daily bike share demand.",
    author="Ambar Gharat",
    author_email="work.ambar09@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("Requirements.txt")
)

