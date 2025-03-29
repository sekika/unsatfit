# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages
from codecs import open
from os import path
import configparser

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read version from unsatfit/data/system.ini

inifile = configparser.ConfigParser()
inifile.read(path.join(here, 'unsatfit/data/system.ini'))
version = inifile.get('system', 'version')

setup(
    name='unsatfit',
    version=version,
    description='Fit soil water retention and unsaturated hydraulic conductivity functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://sekika.github.io/unsatfit/',
    author='Katsutoshi Seki',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Hydrology',
        'Natural Language :: English',
    ],
    keywords='soil',
    packages=find_namespace_packages(include=['unsatfit', 'unsatfit.*']),
    package_data={'unsatfit': ['data/*']},
    install_requires=['numpy', 'scipy', 'matplotlib', 'configparser'],
    include_package_data=True,
    python_requires=">=3.7",
)
