from setuptools import setup, find_packages
from io import open
from os import path
# noinspection PyCompatibility
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Automatically captured required modules for install_requires in requirements.txt
# and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]

dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='fucking-black-scholes',
    description='A simple command line tool for pricing options using the Black-Scholes model',
    version='0.0.1',
    packages=find_packages(),  # List of all packages
    install_requires=install_requires,
    python_requires='>=2.7',  # Any python greater than 2.7
    entry_points='''
        [console_scripts]
        fbs=fbs.main:cli
    ''',
    author="Dennis Concepción Martín",
    keyword="finance, black-scholes, option, pricing, derivative",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/denniscm190/fucking-black-scholes',
    download_url='https://github.com/denniscm190/fucking-black-scholes/archive/0.0.1.tar.gz',
    dependency_links=dependency_links,
    author_email='dennisconcepcionmartin@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
