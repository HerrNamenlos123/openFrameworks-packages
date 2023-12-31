
set(PACKAGE_NAME glfw)
set(LIBRARY_NAME glfw3)
set(FULL_LIBRARY_NAME ${CMAKE_STATIC_LIBRARY_PREFIX}${LIBRARY_NAME}${CMAKE_STATIC_LIBRARY_SUFFIX})

add_library(${PACKAGE_NAME} STATIC IMPORTED)
add_library(${PACKAGE_NAME}::${PACKAGE_NAME} ALIAS ${PACKAGE_NAME})

set_target_properties(${PACKAGE_NAME} 
    PROPERTIES INTERFACE_INCLUDE_DIRECTORIES
    ${CMAKE_CURRENT_LIST_DIR}/$<IF:$<CONFIG:Debug>,debug,release>/include
)

set_target_properties(${PACKAGE_NAME} PROPERTIES IMPORTED_LOCATION_DEBUG ${CMAKE_CURRENT_LIST_DIR}/debug/lib/${FULL_LIBRARY_NAME})
set_target_properties(${PACKAGE_NAME} PROPERTIES IMPORTED_LOCATION_RELEASE ${CMAKE_CURRENT_LIST_DIR}/release/lib/${FULL_LIBRARY_NAME})
set_target_properties(${PACKAGE_NAME} PROPERTIES IMPORTED_LOCATION_MINSIZEREL ${CMAKE_CURRENT_LIST_DIR}/release/lib/${FULL_LIBRARY_NAME})
set_target_properties(${PACKAGE_NAME} PROPERTIES IMPORTED_LOCATION_RELWITHDEBINFO ${CMAKE_CURRENT_LIST_DIR}/release/lib/${FULL_LIBRARY_NAME})