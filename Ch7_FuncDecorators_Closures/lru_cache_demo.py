from clockdeco import clock
import functools


"""
LRU = least-recently used
- Stores results of a previous invocation of an expensive function in the cache
- Avoids recomputing values
- Growth of cache limited by throwing away the least recently used values

TRY WITH AND WITHOUT THE CACHE DECORATOR - IT'S NUTS!
"""

# maxsize == how many call results are stored: POWER OF 2 FOR PERFORMANCE
# typed stores e.g. 1 and 1.0 (int/float) separately
@functools.lru_cache(maxsize=128, typed=False)
@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(26))
