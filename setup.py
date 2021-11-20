from setuptools import setup, find_packages


setup(
    name='fucking-black-scholes',
    description='A simple command line tool for pricing options using the Black-Scholes model',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['numpy~=1.21.4', 'scipy~=1.7.2', 'click~=8.0.3'],
    python_requires='>=3.8',
    entry_points='''
        [console_scripts]
        fbs=fbs.main:cli
    ''',
    author="Dennis Concepción Martín",
    keyword="finance, black-scholes, option, pricing, derivative",
    license='MIT',
    url='https://github.com/denniscm190/fucking-black-scholes',
    author_email='dennisconcepcionmartin@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ]
)
