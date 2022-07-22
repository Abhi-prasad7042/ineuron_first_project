from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    with open("requirements.txt", "r") as f:
        return f.readlines().remove("-e .")

setup(
    name = "housing-predictor",
    version="0.0.1",
    author="abhiprasad7042",
    description="ineuron project",
    packages=["housing"],
    install_requires= get_requirements_list()
)