#!/usr/bin/env python
from setuptools import setup, find_packages


def load_requirements():
    requirements = []
    with open("requirements.txt", "r") as requirements_fd:
        for requirement in requirements_fd:
            if requirement.startswith("#"):
                continue
            requirements.append(requirement.strip())
    return requirements


setup(
    name="ming",
    version="0.0.1",
    python_requires=">=3.11",
    author="Remington Campbell",
    author_email="code@remington.io",
    packages=find_packages(),
    install_requires=load_requirements(),
)
