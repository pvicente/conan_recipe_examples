project(Package CXX)
cmake_minimum_required(VERSION 2.8.12)

include_directories("include")
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
add_executable(example example.cpp)

enable_testing()
add_test(NAME example
        WORKING_DIRECTORY ${EXECUTABLE_OUTPUT_PATH}
        COMMAND example)

