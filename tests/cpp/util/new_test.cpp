
#include "../../../src/cpp/main.cpp"
#include <iostream>
#include <cassert>

void test_add_cpp()
{
    // Test case 1
    int result1 = add_cpp(5, 5);
    assert(result1 == 10);
    std::cout << "[test:cpp] OK" << std::endl;
}

int main()
{
    test_add_cpp();
    return 0;
}