from setuptools import setup, find_packages

setup(
    name='solver',
    version='0.1',
    package_dir={'': 'solver'},
    packages=find_packages(where='solver'),
    install_requires=[],
    description='A small package containing the solver module for my programming lessons. :)',
    author='Fighter',
    author_email='fightingpainter@gmail.com',
    url='https://github.com/Fightingpa1n/ProgrammingLessons',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
