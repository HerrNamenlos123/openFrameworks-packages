
set(LIBRARY_NAME glfw3)
set(FULL_LIBRARY_NAME ${CMAKE_STATIC_LIBRARY_PREFIX}${LIBRARY_NAME}${CMAKE_STATIC_LIBRARY_SUFFIX})

set(LIBRARY_PATH ${CMAKE_CURRENT_LIST_DIR}/$<IF:$<CONFIG:Debug>,debug,release>/${FULL_LIBRARY_NAME})
set(INCLUDE_PATH ${CMAKE_CURRENT_LIST_DIR}/$<IF:$<CONFIG:Debug>,debug,release>/include)

add_library(glfw3 STATIC IMPORTED)
set_target_properties(glfw3 PROPERTIES IMPORTED_LOCATION ${LIBRARY_PATH})
set_target_properties(glfw3 PROPERTIES INTERFACE_INCLUDE_DIRECTORIES ${INCLUDE_PATH})


cmake_minimum_required(VERSION 3.13)
if (MINGW)
    message(STATUS "Using MinGW")
else()
    message(STATUS "Not using MinGW")
endif()