from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="COLORECTRAL_CANCER_PRED",
    version="0.1",
    author="Shreyash",
    packages=find_packages(),
    install_requires=requirements,
)