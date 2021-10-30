# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='nepcal_applet',
    version='0.0.2',
    description='Nepali calendar applet',
    long_description=readme,
    author='Samar Acharya',
    author_email='samar+python@techgaun.com',
    url='https://github.com/techgaun/nepali-calendar-indicator',
    install_requires=['adbs'],
    entry_points="""
    [console_scripts]
    nepcal_applet=nepcalapplet.__init__:main
    """,
    license='Apache-2.0',
    include_package_data = True,
    packages=find_packages(exclude=('tests', 'docs'))
)
