#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:49:21 2017

setup.py file for pymef3 library

Ing.,Mgr. (MSc.) Jan Cimbálník
Biomedical engineering
International Clinical Research Center
St. Anne's University Hospital in Brno
Czech Republic
&
Mayo systems electrophysiology lab
Mayo Clinic
200 1st St SW
Rochester, MN
United States
"""

from setuptools import setup, Extension
import numpy

# the c extension module
MEF_FILE_EXT = Extension("pymef.mef_file.pymef3_file",
                         ["pymef/mef_file/pymef3_file.c"],
                         include_dirs=["pymef/meflib"],
                         extra_compile_args=['-O3'])

setup(name="pymef",
      version='0.1.8',
      description='Wrapper for MEF (multiscale electrophysiology format)',
      url='https://github.com/msel-source/pymef',
      author='Jan Cimbalnik',
      author_email='jan.cimbalnik@fnusa.cz, jan.cimbalnik@mayo.edu',
      license='Apache 2.0',
      platforms=['Linux', 'MaxOSX'],
      keywords='MEF Mayo electrophysiology',
      install_requires=['numpy'],
      zip_safe=False,
      classifiers=['License :: OSI Approved :: Apache Software License',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 4 - Beta',
                   'Topic :: Scientific/Engineering'],
      packages=["pymef", "pymef.mef_file"],
      ext_modules=[MEF_FILE_EXT],
      include_dirs=[numpy.get_include()],
      test_suite='tests')
