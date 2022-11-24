from typing import Callable, Any
import time


def clock(func: Callable[..., Any]) -> Callable[..., Any]:
    def clocked(*args: Any):  # clocked receives any number of positional args
        t0 = time.perf_counter()
        result = func(*args)  # possible to call since 'func' is a free variable
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f"[{elapsed:.8f}s] {name}({arg_str}) -> {result}")
        return result
    return clocked



