from setuptools import setup, find_packages

setup(
    name='algolang',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'algolang = src.__main__:main',
        ],
    },
)