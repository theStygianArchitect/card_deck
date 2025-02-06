# Code Quality

The Deck of Cards library attempts to follow best practices found throughout the internet.
As these practices evolve, our toolsets would change too. 
The Deck of Cards community encourages the proposal of changes and new practices.

## Testing

The Deck of Cards library uses pytest to orchestrate testing.

```shell
uv run python -m pytest tests/
```

## Code linting

[Pylint](https://pylint.readthedocs.io/en/stable/) is a source-code, bug and quality checker.
This check helps validate code quality.

```shell
uv run pylint <python_file_name.py>
```

[Ruff](https://docs.astral.sh/ruff/) is an extremely fast Python linter and code formatter,
written in Rust. 

```shell
uv run pylint <python_file_name.py>
```

## Pep008 checking with pycodestyle

[Pep008](https://www.python.org/dev/peps/pep-0008/) discusses Python
code style. This check helps validate the project is maintains stylistic
consistencies.

```shell
uv run pycodestyle <python_file_name.py>
```

## Pep257 checking with pydocstyle

[Pep257](https://www.python.org/dev/peps/pep-0257) discusses
docstring conventions. This check helps validate docstring
consistencies.

```shell
uv run pydocstyle <python_file_name.py>
```

## Pep484 type hinting with mypy

[Pep484](https://www.python.org/dev/peps/pep-0484) discusses type
hinting. This check helps validate project consistency when type hinting
is used.

```shell
uv run mypy <python_file_name.py>
```

## Static analysis checking with bandit

[Bandit](https://bandit.readthedocs.io/en/latest/) is a tool designed to find common security 
issues. We recommend this tool **NOT** be used to replace enterprise tools, but augment them.

```shell
uv run bandit <python_file_name.py>
```

## Dependency vulnerability checking with pip-audit

[pip-audit](https://github.com/pypa/pip-audit) is a command line tool designed to check your local virtual
environment, your requirement files, or any input from stdin for dependencies with known security 
issues.

```shell
uv run pip-audit
```

## Automating documentation build

A Makefile has been provided to automate the build of Deck of Cards's documentation.
Any changes to Deck of Cards's documentation source files will require a rebuild of the docs. 

```shell
cd ./doc_src && make github
```

## Automating all the checks

A shell script (Deck of Cards-quality-check) has been provided to run automate the above quality checks.

```shell
./quality_check.sh -a
```
