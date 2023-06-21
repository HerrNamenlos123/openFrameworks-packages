add_library(glfw3 STATIC IMPORTED)
set_target_properties(glfw3 PROPERTIES IMPORTED_LOCATION ${GLFW_LIBRARIES})