import re
from pathlib import Path
from aqwebengine import __version__, __author__, __author_email__, __description__

from setuptools import setup, find_packages


setup(
    name="pytest-qasync",
    version=__version__,
    packages=find_packages(),
    url="https://github.com/innodatalabs/aqwebengine",
    license="MIT",
    author="Mike Kroutikov",
    author_email="mkroutikov@innodata.com",
    description="Async helpers for QWebEngine",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">= 3.9",
)
