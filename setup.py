from setuptools import setup, find_packages

setup(
    name='AlexMsg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'am=app.main:main',
        ],
    },
)
