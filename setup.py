#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Stephen Offer",
    author_email='stephen.offer@databricks.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Databricks Data Drift Library",
    entry_points={
        'console_scripts': [
            'db_drift=db_drift.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='db_drift',
    name='db_drift',
    packages=find_packages(include=['db_drift', 'db_drift.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gndctrl2mjrtm/db_drift',
    version='0.1.0',
    zip_safe=False,
)
