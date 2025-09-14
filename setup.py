#!/usr/bin/env python3
"""
Israeli Cyber Security Tools Suite - Advanced Setup Configuration
"""

import os
import sys
from setuptools import setup, find_packages
from pathlib import Path

if sys.version_info < (3, 7):
    raise RuntimeError("Python 3.7+ required")

def read_requirements():
    req_file = Path(__file__).parent / "requirements.txt"
    if req_file.exists():
        with open(req_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="israeli-cyber-security-suite",
    version="2.0.0",
    description="Advanced Israeli Cyber Security Tools Suite",
    long_description="Comprehensive security testing tools for Israeli sites",
    python_requires=">=3.7",
    install_requires=read_requirements(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'israeli-security=main:main',
            'israeli-security-cli=cli_tool:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Security",
    ],
)