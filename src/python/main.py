import ctypes
import os
import time
import sys
from utils import m_perf


# Load the shared library
mylibrary = ctypes.CDLL('D:/projects/game/build/libcpp_module.dll')
mylibrary.sum_numbers_cpp.argtypes = [ctypes.c_int]
mylibrary.sum_numbers_cpp.restype = ctypes.c_int
mylibrary.add_cpp.argtypes = [ctypes.c_int]
mylibrary.add_cpp.restype = ctypes.c_int


@m_perf
def sum_numbers_c():
    mylibrary.sum_numbers_cpp(10000000)


@m_perf
def sum_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def main():
    pass
    p_result = sum_numbers(10000000)
    c_result = sum_numbers_c()
    print(mylibrary.add_cpp(5, 5))


if __name__ == '__main__':
    main()
