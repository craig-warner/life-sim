#!/usr/bin/env python3
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="life-sim", #
    version="1.0.0",
    author="Craig Warner",
    author_email="cgwarner2014@gmail.com",
    description="Life Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craig-warner/life-sim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['argparse>=1.4.0'],
    scripts=['bin/life-sim',
            "bin/version.py"
            ],
)