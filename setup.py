from pip.req import parse_requirements
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prnet',
    version='0.1',
    packages=find_packages(include=['prnet']),
    python_requires='>=3.6, <4',
    install_requires=parse_requirements('requirements.txt'),
    project_urls={  # Optional
        'Source': 'https://github.com/RonnyLV/PRNet/',
    },
)
