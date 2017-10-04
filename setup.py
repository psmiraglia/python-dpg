from setuptools import find_packages
from setuptools import setup

setup(
    name='dpg',
    version='0.1',

    author='Paolo Smiraglia',
    author_email='paolo.smiraglia@gmail.com',
    description='Deterministing Password Generator (DPG)',
    license='To be done...',
    url='https://github.com/psmiraglia/python-dpg',

    packages=find_packages(exclude=['bin', 'docs', 'tests']),
    scripts=['bin/dpg'],
)
