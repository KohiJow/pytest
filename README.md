# Estudos de pytest

Material que montei estudando pytest a fundo, organizado por tema e em ordem de
dificuldade. Cada pasta tem o codigo sendo testado e os testes dele, para poder
rodar e comparar.

A suite toda passa: 70 testes, nenhum warning.

## Os temas

| Pasta | Assunto |
|---|---|
| `2.Intro` | primeiro teste, estrutura e nomenclatura |
| `3.PrimeirosTestes` | asserts e organizacao dos arquivos de teste |
| `4.Fixtures` | fixtures, escopo, setup/teardown e mock de resposta HTTP |
| `5.Parametrizado` | um teste, varios conjuntos de dados |
| `6.Marcadores` | marcadores, selecao e agrupamento de testes |
| `7.Excecoes` | testar que o erro certo acontece |
| `8.Plugins` | testes simples para rodar com plugin de cobertura |
| `10.Integracaoendtoend` | teste de integracao sobre uma app pequena de estoque |
| `11.cicd` | o exemplo minimo que usei para montar o pipeline |
| `12.Avancado` | teste de tempo de execucao e de codigo assincrono |

## Rodando

```bash
pip install -r requirements.txt
pytest -v
```

Um tema por vez:

```bash
pytest 4.Fixtures -v
```

Por marcador (os marcadores estao declarados no `pytest.ini` da raiz, com
`--strict-markers` ligado para nao deixar passar marcador escrito errado):

```bash
pytest -m lento -v
pytest -m "not lento" -v
```

Com cobertura:

```bash
pytest 8.Plugins --cov=8.Plugins
```

## Dependencias

A maior parte dos testes so precisa do pytest. Fora dele:

| O que | Onde |
|---|---|
| `SQLAlchemy` | `4.Fixtures/2setupteardown`, conexao SQLite em memoria no setup/teardown |
| `requests` | `4.Fixtures/1Exemplos/test_mock.py`, so para o `spec` do MagicMock |
| `pytest-asyncio` | `12.Avancado/2.assincrono` |
| `pytest-cov` | cobertura, opcional |

## CI

O workflow fica em `.github/workflows/tests.yml` e roda a suite inteira a cada
push e a cada pull request, em Python 3.10 e 3.12. A pasta `11.cicd` guarda o
exemplo minimo (uma funcao e um teste) que usei para entender o workflow antes
de aplicar no repositorio todo.

## Por que esse repositorio existe

Trabalho com QA e queria sair do "sei escrever um assert" para entender o que o
pytest oferece de verdade: fixture com escopo certo, parametrizacao no lugar de
copiar e colar, marcador para separar o que e rapido do que e lento, e a suite
rodando sozinha num pipeline.
