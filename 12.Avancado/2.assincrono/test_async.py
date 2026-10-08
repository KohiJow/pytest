"""Codigo assincrono com pytest-asyncio.

Uma funcao `async def` precisa de um event loop para rodar; o pytest sozinho
nao sabe disso e o teste terminaria sem nunca ser aguardado. O plugin
pytest-asyncio cuida do loop quando o teste leva `@pytest.mark.asyncio`. O
pyproject.toml esta em `asyncio_mode = "strict"`, entao sem o marcador o teste
nao roda como assincrono.
"""

import asyncio

import pytest

from busca_dados import busca_dados


@pytest.mark.asyncio
async def test_busca_dados() -> None:
    resultado = await busca_dados()
    assert resultado == {"data": "some data"}


@pytest.mark.asyncio
async def test_varias_buscas_ao_mesmo_tempo() -> None:
    """`gather` dispara as corrotinas juntas e devolve os resultados na ordem."""
    resultados = await asyncio.gather(busca_dados(), busca_dados(), busca_dados())
    assert resultados == [{"data": "some data"}] * 3
