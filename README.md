# cmake-python-starter

cmake-python-starter is a CMake project starter that enables binding C++ code to Python. It provides a convenient setup for building C++ projects and includes scripts to easily run Python app, and do Python and C++ tests.

## Getting Started

Follow the instructions below to get started:

### Prerequisites

- CMake
- Python
- g++ Compiler

### Installation

1. Clone the repository:

   git clone https://github.com/Mokke29/cmake-python-starter.git
2. Build the project using CMake:
    cd cmake-python-starter
    mkdir build
    cd build
    cmake ..
    python ./build.py

## Usage

### Building C++
    python ./build.py

### Running main Python script:
    python ./run.py

## Running Tests

You can run the tests using the provided test script (`test.py`). Here are the available options:

### Run one given Python test:
    python ./test.py util.add_test

### Run all Python tests:
    python ./test.py all

### Run all C++ tests:
    python ./test.py cpp