"""Corrotina de exemplo, testada em `test_async.py`."""

import asyncio


async def busca_dados() -> dict[str, str]:
    await asyncio.sleep(0.1)  # simula a espera por uma resposta de rede
    return {"data": "some data"}
