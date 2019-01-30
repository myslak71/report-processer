import os

from setuptools import setup, find_packages

DIR_PATH = os.path.dirname(
    os.path.abspath(__file__))

with open(os.path.join(DIR_PATH, 'README.md')) as file:
    long_description = file.read()

install_requires = [line.rstrip('\n') for line in open(
    os.path.join(DIR_PATH, 'requirements.txt'))]

setup(
    name='csv-report-processer',
    version='0.1.0',
    packages=find_packages(),
    author='myslak71',
    author_email='kornel.szurek@protonmail.com',
    description='CSV report processor for Clearcode',
    long_description=long_description,
    install_requires=install_requires
)
