from setuptools import setup, find_namespace_packages
from os.path import abspath, dirname, join

# Fetches the content from README.md
# This will be used for the "long_description" field.
README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name="chessfessor",
    version="1.0.10",
    packages=find_namespace_packages(include=['chessfessor', 'chessfessor.*'], exclude=['*.tests*']),
    description="Extract your chess games data from https://lichess.org and https://chess.com",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/FrequentlyMissedDeadlines/py-chessfessor",
    author="FrequentlyMissedDeadlines",
    author_email="FrequentlyMissedDeadlines+chessfessor@gmail.com",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Games/Entertainment :: Board Games",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    project_urls={
        'Bug Reports': 'https://github.com/FrequentlyMissedDeadlines/py-chessfessor/issues',
        'Source': 'https://github.com/FrequentlyMissedDeadlines/py-chessfessor',
    },
)