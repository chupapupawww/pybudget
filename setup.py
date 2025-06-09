from setuptools import setup, find_packages

setup(
    name='pybudget',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'pandas',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': ['pybudget=pybudget.cli:main'],
    },
)
