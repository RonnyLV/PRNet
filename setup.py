from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='prnet',
    version='0.1',
    packages=find_packages(include=['prnet']),
    python_requires='>=3.6, <4',
    install_requires=install_requires,
    project_urls={  # Optional
        'Source': 'https://github.com/RonnyLV/PRNet/',
    },
)
