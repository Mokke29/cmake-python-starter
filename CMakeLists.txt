cmake_minimum_required(VERSION 3.26.4)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(cmake_python VERSION 0.1)

set(SOURCES
    src/cpp/main.cpp
)

set(HEADERS
    include/main.h
)

add_library(cpp_module SHARED ${SOURCES})

set_target_properties(cpp_module PROPERTIES OUTPUT_NAME "cpp_module")
set_target_properties(cpp_module PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")

install(TARGETS cpp_module DESTINATION lib)

install(FILES include/main.h DESTINATION include)
