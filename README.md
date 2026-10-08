# Estudos de pytest

Material que montei estudando pytest a fundo, organizado por tema e em ordem de
dificuldade. Cada pasta tem o codigo sendo testado e os testes dele, para poder
rodar e comparar.

## Os temas

| Pasta | Assunto |
|---|---|
| `2.Intro` | primeiro teste, estrutura e nomenclatura |
| `3.PrimeirosTestes` | asserts, organizacao em classes |
| `4.Fixtures` | fixtures, escopo e reaproveitamento de setup |
| `5.Parametrizado` | um teste, varios conjuntos de dados |
| `6.Marcadores` | marcadores, selecao e agrupamento de testes |
| `7.Excecoes` | testar que o erro certo acontece |
| `8.Plugins` | plugins do ecossistema |
| `10.Integracaoendtoend` | teste de integracao sobre uma app pequena |
| `11.cicd` | a mesma suite rodando no GitHub Actions |
| `12,Avancado` | performance e testes de codigo assincrono |

## Rodando

```bash
pip install pytest
pytest -v
```

Um tema por vez:

```bash
pytest pytest/Pytest/4.Fixtures -v
```

Por marcador:

```bash
pytest -m lento -v
```

## Por que esse repositorio existe

Trabalho com QA e queria sair do "sei escrever um assert" para entender o que o
pytest oferece de verdade: fixture com escopo certo, parametrizacao no lugar de
copiar e colar, marcador para separar o que e rapido do que e lento, e a suite
rodando sozinha num pipeline.

O modulo `11.cicd` e o que mais uso como referencia: tem o workflow do GitHub
Actions que roda os testes a cada push.
