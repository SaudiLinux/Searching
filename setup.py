#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف إعداد أداة بحث SQL المتقدمة
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sql-search-tool",
    version="1.0.0",
    author="SayerLinux",
    author_email="SayerLinux1@gmail.com",
    description="أداة بحث SQL المتقدمة لمسح خوادم قواعد البيانات",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaudiLinux",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: Database",
        "Topic :: Internet",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "sql-search=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.svg", "*.md"],
    },
)