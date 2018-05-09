#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

# RELEASE STEPS
# $ python setup.py bdist_wheel
# $ python twine upload dist/VX.Y.Z.whl
# $ git tag -a VX.Y.Z -m "release version VX.Y.Z"
# $ git push origin VX.Y.Z

NAME = "appearance-score"
VERSION = "0.1.0"
URL = "https://github.com/chenjiandongx/Microsoft-appearance-score"
AUTHOR = "chenjiandongx"
AUTHOR_EMAIL = "chenjiandongx@qq.com"
LICENSE = "MIT"
REQUIRES = ["requests"]
MODULES = ["core"]
DESC = "微软小冰颜值测试命令行工具"


setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    version=VERSION,
    license=LICENSE,
    install_requires=REQUIRES,
    url=URL,
    py_modules=MODULES,
    description=DESC,
    entry_points={"console_scripts": ["mas=core:command_line_runner"]},
)
