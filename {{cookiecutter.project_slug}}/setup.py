#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open
import os
import re

from setuptools import find_packages, setup


current_dir = os.path.dirname(os.path.realpath(__file__))
with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()


def get_meta():
    meta_re = re.compile(r"(?P<name>__\w+__) = '(?P<value>[^']+)'")
    meta_d = {}
    with open(os.path.join(current_dir, '{{ cookiecutter.module_name }}/__init__.py'),
              encoding='utf8') as fp:
        for match in meta_re.finditer(fp.read()):
            meta_d[match.group('name')] = match.group('value')
    return meta_d


requirements = [
    # TODO: put package requirements here
]

extras_require = {
    '': requirements,
    # ':python_version<"2.7"': ['argparse'],
    # ':python_version<"3.4"': ['enum34'],
}

meta_d = get_meta()
setup(
    name='{{ cookiecutter.project_slug }}',
    version=meta_d['__version__'],
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']
    ),
    package_dir={'{{ cookiecutter.module_name }}':
                 '{{ cookiecutter.module_name }}'},
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    license='MIT',
    zip_safe=False,
    # entry_points={
    #     'console_scripts': [
    #         '{{ cookiecutter.module_name }} = {{ cookiecutter.module_name }}.__main__:main',
    #     ],
    # },
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
