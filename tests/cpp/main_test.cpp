#include "../../src/cpp/main.cpp"
#include <iostream>
#include <cassert>

void test_sum_numbers()
{
    // Test case 1
    int result1 = sum_numbers_cpp(5);
    assert(result1 == 15);

    // Test case 2
    int result2 = sum_numbers_cpp(10);
    assert(result2 == 55);

    // Test case 3
    int result3 = sum_numbers_cpp(0);
    assert(result3 == 0);

    std::cout << "[test:cpp] OK" << std::endl;
}

int main()
{
    test_sum_numbers();
    return 0;
}