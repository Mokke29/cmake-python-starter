#include "../../include/main.h"

int sum_numbers_cpp(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; ++i)
    {
        sum += i;
    }
    return sum;
}

int add_cpp(int a, int b)
{
    return a + b;
}