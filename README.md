# py-chessfessor
[![Build](https://github.com/FrequentlyMissedDeadlines/py-chessfessor/actions/workflows/python-package.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/py-chessfessor/actions/workflows/python-package.yml)
[![Publish](https://github.com/FrequentlyMissedDeadlines/py-chessfessor/actions/workflows/python-publish.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/py-chessfessor/actions/workflows/python-publish.yml)
[![Version](https://img.shields.io/pypi/v/chessfessor)](https://pypi.org/project/chessfessor)
[![Version](https://img.shields.io/pypi/pyversions/chessfessor)](https://pypi.org/project/chessfessor)
[![codecov](https://codecov.io/gh/FrequentlyMissedDeadlines/py-chessfessor/branch/main/graph/badge.svg)](https://codecov.io/github/FrequentlyMissedDeadlines/py-chessfessor?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Downloads](https://img.shields.io/pypi/dm/chessfessor)

Chessfessor is the short for "Chess Professor". This command line tool will allow you to download all your chess game data from [Lichess](https://lichess.org/) and [Chess.com](https://www.chess.com/). You can then put this data in any BI tool you like to analyse your games or generate dashboards like winrates per opening.

## Install

```
python -m pip install chessfessor
```

## Usage

```
chessfessor Kasparov
```

## Advanced usage

```bash
# Display help page
chessfessor -h

# Get Lichess.org games for player Kasparov
chessfessor Kasparov --website lichess

# Get Chess.com games for player Kasparov
chessfessor Kasparov --website chessdotcom

#Get Lichess.org games for player Kasparov, including casual games
chessfessor Kasparov --website lichess --include-casual
```

## Disclaimer
I have no rights on [Lichess](https://lichess.org/) or [Chess.com](https://www.chess.com/). All rights belong to their respective owners.

But this tool comes from free, enjoy it! 🎉