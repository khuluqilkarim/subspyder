# setup.py

from setuptools import setup, find_packages

setup(
    name='subspyder',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'subspyder=my_module.main:main',
        ],
    },
)
