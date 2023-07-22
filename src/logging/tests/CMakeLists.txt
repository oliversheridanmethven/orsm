add_executable(example_logging example_logging.c)
add_executable(example_logging_cpp example_logging.cpp)
TARGET_LINK_LIBRARIES(example_logging ${GLIB_LIBRARIES})
TARGET_LINK_LIBRARIES(example_logging_cpp ${GLIB_LIBRARIES})