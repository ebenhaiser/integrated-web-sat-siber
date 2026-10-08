import asyncio
import time


async def worker(name: str):
    print(f"[{name}] START")

    await asyncio.sleep(2)

    print(f"[{name}] END")


async def run_parallel():
    start = time.perf_counter()

    await asyncio.gather(
        worker("MODEL-1"),
        worker("MODEL-2")
    )

    return time.perf_counter() - start


def test_concurrency():
    duration = asyncio.run(run_parallel())

    print(f"\nTotal execution time: {duration:.2f}s")

    assert duration < 3