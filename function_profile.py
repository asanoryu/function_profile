"""Provide a decorator for measuring function execute time and memory usage."""
import time
from functools import wraps
from memory_profiler import memory_usage


def profile(fn):
    """Wrap a function and call it 2 times - once to measure time and once for memory."""

    @wraps(fn)
    def inner(*args, **kwargs):
        fn_kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"\n{fn.__name__}({fn_kwargs_str})")

        # Measure time
        t = time.perf_counter()
        retval = fn(*args, **kwargs)
        elapsed = time.perf_counter() - t
        print(f"Time   {elapsed:0.4}")

        # Measure memory
        mem, retval = memory_usage(
            (fn, args, kwargs), retval=True, timeout=200, interval=1e-7
        )

        print(f"Memory {max(mem) - min(mem)}")
        return retval

    return inner
