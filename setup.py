# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


long_desc = '''
sphinx-rfcsection is a minimal Sphinx extension to add sane automatic titles
to RFC references with sections included.

Any RFC reference that consists of just the RFC number, or that specifies a
custom title, is passed directly to Sphinx's built-in `:rfc:` role untouched.
'''


setup(
    name='sphinx-rfcsection',
    version='0.1.0',
    url='https://github.com/dgw/sphinx-rfcsection',
    download_url='https://pypi.org/project/sphinx-rfcsection/',
    author='dgw',
    author_email='dgw@technobabbl.es',
    description="sphinx-rfcsection smartly titles links to RFC sections",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    python_requires=">=3.6",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
)
