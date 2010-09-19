
"""Setup"""

__author__ = 'Andy Theyers <andy.theyers@isotoma.com>'
__docformat__ = 'restructuredtext en'

import os

from setuptools import find_packages
from setuptools import setup

execfile(os.path.join(os.path.dirname(__file__), "currentcost", "release.py"))

long_description = """Connect to your currentcost electricity meter and 
pump data to a variety of data collection facilities. Pluggable, so new
data stores are easily added."""

setup(
    name="currentcost",
    packages=find_packages(),
    version=version,
    description=description,
    long_description=long_description,
    author=author,
    author_email=email,
    download_url=download_url,
    install_requires=[
        'mutagen',
        'nose',
        ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        ],
    )
