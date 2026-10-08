# Estudos de pytest

Material que montei estudando pytest a fundo, organizado por tema e em ordem de
dificuldade. Cada pasta tem o codigo sendo testado e os testes dele, e cada
arquivo comeca com uma docstring explicando o conceito que ele mostra. A ideia
e ler na ordem, rodar um tema por vez e mexer no codigo para ver o que quebra.

A suite toda passa: 94 testes, nenhum warning, em Python 3.9, 3.11 e 3.12.

## Como rodar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Toda a configuracao fica no `pyproject.toml`, o unico arquivo de configuracao
do repositorio: marcadores registrados, modo do pytest-asyncio e regras do
ruff, cada bloco com um comentario dizendo o porque.

## Trilha de estudo

A numeracao das pastas e a ordem original do estudo e tem buracos (nao existe
1 nem 9); preferi manter os numeros a renumerar tudo. A ordem de leitura
sugerida e a da tabela.

| Ordem | Pasta | O que ensina | Rodar so isso |
|---|---|---|---|
| 1 | `2.Intro` | como o pytest acha arquivos e funcoes de teste, e o que ele mostra quando um `assert` falha | `pytest 2.Intro -v` |
| 2 | `3.PrimeirosTestes` | varios asserts num teste, teste que importa o codigo de outro modulo, mensagem no assert, diff de listas e dicts | `pytest 3.PrimeirosTestes -v` |
| 3 | `4.Fixtures` | fixture basica, `conftest.py`, mock de resposta HTTP com `spec`, setup e teardown com `yield`, escopo function, module e session | `pytest 4.Fixtures -v` |
| 4 | `5.Parametrizado` | `parametrize` simples, ids legiveis com `pytest.param`, casos de fronteira, `approx` para float, parametrize empilhado (produto cartesiano) | `pytest 5.Parametrizado -v` |
| 5 | `6.Marcadores` | marcadores registrados, selecao com `-m` e expressoes booleanas, `--strict-markers` | `pytest 6.Marcadores -v` |
| 6 | `7.Excecoes` | `pytest.raises`, `match` para conferir a mensagem, `exc_info.value` | `pytest 7.Excecoes -v` |
| 7 | `8.Plugins` | pytest-cov: medir cobertura e exigir um minimo | `pytest 8.Plugins --cov=8.Plugins` |
| 8 | `10.Integracaoendtoend` | teste de integracao com os objetos reais e uma fixture que entrega estado limpo | `pytest 10.Integracaoendtoend -v` |
| 9 | `11.cicd` | o projeto minimo que usei para montar o workflow do GitHub Actions | `pytest 11.cicd -v` |
| 10 | `12.Avancado` | teste de tempo de execucao com relogio falso (`monkeypatch`) e teste assincrono com pytest-asyncio | `pytest 12.Avancado -v` |

Para rodar um unico teste, use `-k` com um pedaco do nome ou o id completo:

```bash
pytest 5.Parametrizado -k fronteira -v
pytest "5.Parametrizado/2classificacao/test_classifica_idade.py::test_classifica_idade[fronteira_adulto]"
```

## Por marcador

Os marcadores estao declarados no `pyproject.toml` com `--strict-markers`
ligado: marcador escrito errado e erro de coleta, nao aviso.

```bash
pytest -m lento -v              # so os quatro testes lentos (uns 7 segundos)
pytest -m "not lento"           # a suite inteira em cerca de um segundo
pytest -m "lento and not rapido" -v
pytest -m adulto -v             # marcadores da atividade de 6.Marcadores
```

## Cobertura

```bash
pytest 8.Plugins --cov=8.Plugins --cov-report=term-missing
pytest 8.Plugins --cov=8.Plugins --cov-fail-under=100
```

A segunda forma falha se a cobertura cair abaixo de 100%; e o que o CI roda.

## Lint e formatacao

```bash
ruff check .          # regras selecionadas no pyproject.toml
ruff format --check . # ou `ruff format .` para aplicar
```

O alvo e Python 3.9, entao o ruff nao sugere sintaxe mais nova (nada de
`match`, nem `X | Y` em anotacao). Onde um tipo pode ser `None`, o codigo usa
`Optional` do `typing`.

## Por que nao tem `__init__.py`

Os testes importam o codigo pelo nome do modulo (`from soma import soma`).
Isso funciona porque, sem `__init__.py`, o pytest insere a pasta de cada
arquivo de teste no `sys.path` antes de importa-lo (modo de import `prepend`,
o padrao). A unica regra e que o nome de cada modulo e de cada arquivo de
teste seja unico no repositorio inteiro. A lista desses modulos esta em
`known-first-party` no `pyproject.toml`, para o ruff agrupar os imports
direito.

## Dependencias

A maior parte dos testes so precisa do pytest. Fora dele:

| O que | Onde |
|---|---|
| `SQLAlchemy` | `4.Fixtures/2setupteardown`, SQLite em memoria no setup/teardown |
| `requests` | `4.Fixtures/1Exemplos/test_mock.py`, so para o `spec` do MagicMock |
| `pytest-asyncio` | `12.Avancado/2.assincrono` |
| `pytest-cov` | cobertura em `8.Plugins` e no CI |
| `ruff` | lint e formatacao |

## CI

O workflow em `.github/workflows/tests.yml` roda a cada push e pull request,
em dois jobs: `ruff` (lint e formatacao) e `pytest`, este numa matriz com
Python 3.9, 3.11 e 3.12. Depois da suite, o job de testes roda a cobertura de
`8.Plugins` com `--cov-fail-under=100`.

A pasta `11.cicd` guarda o exemplo minimo (uma funcao, um teste e um
`requirements.txt` so com pytest) que usei para entender o workflow antes de
aplicar no repositorio todo.

## Por que esse repositorio existe

Trabalho com QA e queria sair do "sei escrever um assert" para entender o que o
pytest oferece de verdade: fixture com escopo certo, parametrizacao no lugar de
copiar e colar, marcador para separar o que e rapido do que e lento, e a suite
rodando sozinha num pipeline.
