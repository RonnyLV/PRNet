from os import path

from setuptools import setup


def download_models():
    download_command = ['bash', './download_models.sh', '1UoE-XuW1SDLUjZmJPkIZ1MLxvQFgmTFH',
                        './prnet/assets/net-data/56_256_resfcn256_weight.data-00000-of-00001']
    import subprocess
    process = subprocess.Popen(download_command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='prnet',
    version='0.1',
    packages=[
        'prnet',
        'prnet.utils'
    ],
    package_dir={'prnet': 'prnet'},
    package_data={
        'prnet': [
            'assets/net-data/*',
            'assets/uv-data/*'
        ]
    },
    python_requires='>=3.6, <4',
    install_requires=install_requires,
    project_urls={  # Optional
        'Source': 'https://github.com/RonnyLV/PRNet/',
    },
)
