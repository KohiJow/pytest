# pytest studies
English | [Português](README.pt-BR.md)

Material I put together while studying pytest in depth, organized by topic and
in order of difficulty. Each folder has the code under test and its tests, and
each file starts with a docstring explaining the concept it shows. The idea is
to read in order, run one topic at a time and tinker with the code to see what
breaks.

The whole suite passes: 94 tests, no warnings, on Python 3.9, 3.11 and 3.12.

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

All the configuration lives in `pyproject.toml`, the only configuration file in
the repository: registered markers, the pytest-asyncio mode and the ruff rules,
each block with a comment explaining why.

## Study path

The folder numbering is the original order of study and has gaps (there is no
1 and no 9); I preferred to keep the numbers rather than renumber everything.
The suggested reading order is the one in the table.

| Order | Folder | What it teaches | Run just this |
|---|---|---|---|
| 1 | `2.Intro` | how pytest finds test files and functions, and what it shows when an `assert` fails | `pytest 2.Intro -v` |
| 2 | `3.PrimeirosTestes` | several asserts in one test, a test that imports code from another module, a message in the assert, diffs of lists and dicts | `pytest 3.PrimeirosTestes -v` |
| 3 | `4.Fixtures` | basic fixture, `conftest.py`, mocking an HTTP response with `spec`, setup and teardown with `yield`, scope (function, module and session) | `pytest 4.Fixtures -v` |
| 4 | `5.Parametrizado` | simple `parametrize`, readable ids with `pytest.param`, boundary cases, `approx` for floats, stacked parametrize (Cartesian product) | `pytest 5.Parametrizado -v` |
| 5 | `6.Marcadores` | registered markers, selection with `-m` and boolean expressions, `--strict-markers` | `pytest 6.Marcadores -v` |
| 6 | `7.Excecoes` | `pytest.raises`, `match` to check the message, `exc_info.value` | `pytest 7.Excecoes -v` |
| 7 | `8.Plugins` | pytest-cov: measuring coverage and requiring a minimum | `pytest 8.Plugins --cov=8.Plugins` |
| 8 | `10.Integracaoendtoend` | integration test with the real objects and a fixture that provides a clean state | `pytest 10.Integracaoendtoend -v` |
| 9 | `11.cicd` | the minimal project I used to set up the GitHub Actions workflow | `pytest 11.cicd -v` |
| 10 | `12.Avancado` | an execution time test with a fake clock (`monkeypatch`) and an async test with pytest-asyncio | `pytest 12.Avancado -v` |

To run a single test, use `-k` with part of its name, or the full id:

```bash
pytest 5.Parametrizado -k fronteira -v
pytest "5.Parametrizado/2classificacao/test_classifica_idade.py::test_classifica_idade[fronteira_adulto]"
```

## By marker

The markers are declared in `pyproject.toml` with `--strict-markers` turned on:
a misspelled marker is a collection error, not a warning.

```bash
pytest -m lento -v              # so os quatro testes lentos (uns 7 segundos)
pytest -m "not lento"           # a suite inteira em cerca de um segundo
pytest -m "lento and not rapido" -v
pytest -m adulto -v             # marcadores da atividade de 6.Marcadores
```

## Coverage

```bash
pytest 8.Plugins --cov=8.Plugins --cov-report=term-missing
pytest 8.Plugins --cov=8.Plugins --cov-fail-under=100
```

The second form fails if coverage drops below 100%; that is what CI runs.

## Linting and formatting

```bash
ruff check .          # regras selecionadas no pyproject.toml
ruff format --check . # ou `ruff format .` para aplicar
```

The target is Python 3.9, so ruff does not suggest newer syntax (no `match`,
and no `X | Y` in annotations). Where a type can be `None`, the code uses
`Optional` from `typing`.

## Why there is no `__init__.py`

The tests import the code by module name (`from soma import soma`). This works
because, without `__init__.py`, pytest inserts the folder of each test file into
`sys.path` before importing it (the `prepend` import mode, which is the
default). The only rule is that the name of every module and every test file
must be unique across the whole repository. The list of these modules is in
`known-first-party` in `pyproject.toml`, so that ruff groups the imports
correctly.

## Dependencies

Most of the tests only need pytest. Beyond that:

| What | Where |
|---|---|
| `SQLAlchemy` | `4.Fixtures/2setupteardown`, in-memory SQLite in setup/teardown |
| `requests` | `4.Fixtures/1Exemplos/test_mock.py`, only for the MagicMock `spec` |
| `pytest-asyncio` | `12.Avancado/2.assincrono` |
| `pytest-cov` | coverage in `8.Plugins` and in CI |
| `ruff` | linting and formatting |

## CI

The workflow in `.github/workflows/tests.yml` runs on every push and pull
request, in two jobs: `ruff` (linting and formatting) and `pytest`, the latter
in a matrix with Python 3.9, 3.11 and 3.12. After the suite, the test job runs
coverage on `8.Plugins` with `--cov-fail-under=100`.

The `11.cicd` folder holds the minimal example (one function, one test and a
`requirements.txt` with only pytest) that I used to understand the workflow
before applying it to the whole repository.

## Why this repository exists

I work in QA and wanted to move from "I know how to write an assert" to
understanding what pytest really offers: fixtures with the right scope,
parametrization instead of copy and paste, markers to separate what is fast
from what is slow, and the suite running on its own in a pipeline.
