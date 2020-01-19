import os

from setuptools import setup, find_packages

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR_PATH, 'README.md'), encoding='utf8') as file:
    long_description = file.read()

install_requires = [line.rstrip('\n') for line in open(
    os.path.join(DIR_PATH, 'requirements.txt'))]

setup(
    name='csv_report_processer',
    version='1.0.0',
    packages=find_packages(exclude=('tests', 'example')),
    author='myslak71',
    author_email='myslak@protonmail.com',
    description='CSV report processor for Clearcode',
    long_description=long_description,
    install_requires=install_requires,
    python_requires=">=3.7",
    include_package_data=True,
    entry_points={
        'console_scripts': ['csv-report-processer=csv_report_processer.cli:main'],
    }

)
