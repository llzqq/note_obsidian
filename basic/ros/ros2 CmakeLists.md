```txt
cmake_minimum_required(VERSION 3.8)
project(read_depth_image)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 找到依赖项
find_package(OpenCV 4 REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)

# 添加可执行文件
add_executable(read_depth_image_node src/read_depth_image.cpp)

# 链接ROS2包
ament_target_dependencies(read_depth_image_node
rclcpp
sensor_msgs
cv_bridge
OpenCV
)

# 安装可执行文件
install(TARGETS
read_depth_image_node
DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch
DESTINATION share/${PROJECT_NAME}
)

# 导出依赖项，让其他ROS2包能够使用这个包
ament_export_dependencies(rclcpp sensor_msgs cv_bridge OpenCV)
ament_package()
```
