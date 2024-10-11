from setuptools import setup, find_packages

setup(
    name='programming_lessons',
    version='0.1',
    package_dir={'': 'py_package'},
    packages=find_packages(where='py_package'),
    install_requires=[],
    description='Programming lessons python package containing stuff needed for things to work',
    author='Fighter',
    author_email='fightingpainter@gmail.com',
    url='https://github.com/Fightingpa1n/ProgrammingLessons',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
