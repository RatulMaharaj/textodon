#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "Click>=7.0",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Ratul Maharaj",
    author_email="ratulmaharaj@looped.co.za",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A TUI mastodon client & CLI",
    entry_points={
        "console_scripts": [
            "textodon=textodon.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="textodon",
    name="textodon",
    packages=find_packages(include=["textodon", "textodon.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/RatulMaharaj/textodon",
    version="0.1.0",
    zip_safe=False,
)
