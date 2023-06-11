cmake_minimum_required(VERSION 3.26.0-msvc3)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(cmake_python VERSION 0.1)

set(SOURCES
    src/cpp/main.cpp
)

set(HEADERS
    include/main.h
)

# set(RAYLIB_VERSION 4.5.0)
# find_package(raylib ${RAYLIB_VERSION} QUIET) # QUIET or REQUIRED
# if (NOT raylib_FOUND) # If there's none, fetch and build raylib
#   include(FetchContent)
#   FetchContent_Declare(
#     raylib
#     DOWNLOAD_EXTRACT_TIMESTAMP OFF
#     URL https://github.com/raysan5/raylib/archive/refs/tags/${RAYLIB_VERSION}.tar.gz
#   )
#   FetchContent_GetProperties(raylib)
#   if (NOT raylib_POPULATED) # Have we downloaded raylib yet?
#     set(FETCHCONTENT_QUIET NO)
#     FetchContent_Populate(raylib)
#     set(BUILD_EXAMPLES OFF CACHE BOOL "" FORCE) # don't build the supplied examples
#     add_subdirectory(${raylib_SOURCE_DIR} ${raylib_BINARY_DIR})
#   endif()
# endif()

add_library(cpp_module SHARED ${SOURCES})

set_target_properties(cpp_module PROPERTIES OUTPUT_NAME "cpp_module")
set_target_properties(cpp_module PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")

install(TARGETS cpp_module DESTINATION lib)

install(FILES include/main.h DESTINATION include)

#target_link_libraries(cpp_module PRIVATE raylib)