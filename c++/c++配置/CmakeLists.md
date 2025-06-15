#### 模板
```
cmake_minimum_required(VERSION 3.0.2)
project(followbot)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -ggdb -Wall ")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/build/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/build)

set(OpenCV_DIR /usr/local/share/OpenCV)
find_package(OpenCV 3.4.12 REQUIRED)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  sensor_msgs
  cv_bridge
)

catkin_package(
 CATKIN_DEPENDS geometry_msgs rospy sensor_msgs
#  DEPENDS system_lib
)

catkin_install_python(PROGRAMS
  scripts/followbot.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

-----------------------------------------------------------

find_package是本包需要的ros依赖
catkin_package是其他包引用本包需要的依赖
numpy是python包，被python环境自带，看安装的位置也能看出来
```
#### 指定package
```
#指定.cmake文件
set(cv_bridge_DIR /usr/local/cv_bridge_foropencv3/usr/local/share/cv_bridge/cmake)
find_package(cv_bridge REQUIRED)

set(OpenCV_DIR /usr/local/share/OpenCV)
find_package(OpenCV 3.4.12 REQUIRED)

指定.so
set(CMAKE_PREFIX_PATH "/usr/local/glog" ${CMAKE_PREFIX_PATH})
find_package(glog REQUIRED)

----------orbslam3安装-----------
/home/lzq/packges/ORB_SLAM3_detailed_comments/ros/src/orbslam3
有很多编译知识
```

#### opencv3位置
```
set(OpenCV_DIR /usr/local/share/OpenCV)
set(OpenCV_INCLUDE_DIRS "/usr/local/include/opencv2")
set(OpenCV_LIBRARIES "/usr/local/lib")
```
#### opencv版本冲突
```
set(LIBS 
...
/usr/local/lib/libopencv_core.so.3.4
/usr/local/lib/libopencv_imgproc.so.3.4
/usr/lib/x86_64-linux-gnu/libopencv_core.so.4.2
/usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.4.2
)
```