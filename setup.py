import os
from setuptools import setup, find_packages
import naturalcropping
 
LONG_DESCRIPTION = open('README.rst').read()
 
setup(
    name='naturalcropping',
    version=naturalcropping.__version__,
    description="Natural cropping for sorl-thumbnail",
    long_description=LONG_DESCRIPTION,
    author=naturalcropping.__author__,
    author_email='sun.void@gmail.com',
    keywords='django',
    url='http://github.com/uruz/naturalcropping',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['sorl-thumbnail'],
    zip_safe=False,

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)