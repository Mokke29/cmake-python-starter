import ctypes
import time
try:
    from utils import m_perf
except:
    from src.python.utils import m_perf


# Load the shared library
mylibrary = ctypes.CDLL('D:/projects/game/build/libgame_modules.dll')

# Declare the prototypes
mylibrary.my_function.argtypes = [ctypes.c_int]
mylibrary.my_function.restype = ctypes.c_int

mylibrary.sum_numbers.argtypes = [ctypes.c_int]
mylibrary.sum_numbers.restype = ctypes.c_int


@m_perf
def sum_numbers_c():
    mylibrary.sum_numbers(10000000)


@m_perf
def sum_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def main():

    p_result = sum_numbers(10000000)
    c_result = sum_numbers_c()


if __name__ == '__main__':
    main()
