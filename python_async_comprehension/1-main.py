#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    valor = await async_comprehension()
    print(valor)
    print(type(valor))

asyncio.run(main())