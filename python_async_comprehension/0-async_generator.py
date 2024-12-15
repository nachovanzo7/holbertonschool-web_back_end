    #!/usr/bin/env python3
    """
    python
    """

    import random
    import asyncio
    from typing import Generator


    async def async_generator() -> Generator[float, None, None]:
        """
        Generador asincrono entre 0 and 10.

        Yields:
            float: Random float
        """
        for _ in range(10):
            await asyncio.sleep(1)  # Simulate asynchronous operation
            yield random.uniform(0, 10)
