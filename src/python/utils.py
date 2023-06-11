
import time
from colorama import Fore, Style


def m_perf(func):
    """
    A decorator for measuring the performance of the function.

    Parameters:
        func (callable)

    Returns:
        callable: The decorated function.

    Example:
        @m_perf
        def my_function():
            # Function implementation

        my_function()  # Calls the decorated function, measuring its performance.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration_ms = (end_time - start_time) * 1000
        time_string = f"[m_perf] {func.__name__}: {duration_ms} ms"
        print(f"{Fore.LIGHTMAGENTA_EX}{time_string}{Style.RESET_ALL}")

        return result

    return wrapper
