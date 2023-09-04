from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'package training watch'
LONG_DESCRIPTION = 'Testing if i remember anything from last package'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="watch",
    version=VERSION,
    author="Bocianski",
    author_email="szyper212pl@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    #install_requires=open("requirements.txt").readlines(),

    keywords=['python', 'watch', 'time', 'date'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)