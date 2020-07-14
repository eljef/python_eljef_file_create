# -*- coding: UTF-8 -*-
"""Setup script"""

from setuptools import setup

setup(
    author='Jef Oliver',
    author_email='jef@eljef.me',
    description='File Creation Utilities',
    install_requires=['eljef_core>=1.2.2'],
    license='LGPLv2.1',
    name='eljef_file_create',
    packages=['eljef.file_create', 'eljef.file_create.cli', 'eljef.file_create.files',
              'eljef.file_create.licenses'],
    python_requires='>=3.8',
    url='https://github.com/eljef/python_eljef_file_create',
    version='0.2.0',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ej-file-create = eljef.file_create.cli.__main__:main'
        ]
    },
)
