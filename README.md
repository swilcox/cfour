[![Testing Status](https://github.com/swilcox/cfour/actions/workflows/testing.yaml/badge.svg)](https://github.com/swilcox/cfour/actions/workflows/testing.yaml)

CFour
=====

A super simple connect four type game engine and a CLI frontend for using it.

Python (3.11+)

## Tests

This project uses [pdm](https://github.com/pdm-project/pdm):

```
pdm install
```

Then execute the tests:
```
pdm run py.test
```

## CLI Frontend

```
pdm run python cli_four.py
```

## TO-DO

* web back-end
* web frontend
* engine optimizations
* color/curses implementation
* move history/undo
* docs
* more tests

