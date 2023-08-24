from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='PicFetch',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    description='Receive images from the internet or local. Save them anywhere in the memory. Display a single image or multiple images. ',
    author='MahsaSanaei',
    author_email='mahsasanaei.n@gmail.com',
    )