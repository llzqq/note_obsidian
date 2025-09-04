
#### 指定package位置
```
# 指定.cmake文件
set(cv_bridge_DIR /usr/local/cv_bridge_foropencv3/usr/local/share/cv_bridge/cmake)
find_package(cv_bridge REQUIRED)

set(OpenCV_DIR /usr/local/share/OpenCV)
find_package(OpenCV 3.4.12 REQUIRED)

# 指定.so
set(OpenCV_LIBRARIES "/usr/local/lib")

# 指定.h
set(OpenCV_INCLUDE_DIRS "/usr/local/include/opencv2")
```

**CmakeLists中指定了包路径，
但不一定会链接到该路径下的包，
有很多种其他情况，尤其是在安装了多个版本的情况下**
#### 遇到麻烦的库依赖
```
# 直接把所有需要库具体位置写出来
set(LIBS 
...
/usr/local/lib/libopencv_core.so.3.4
/usr/local/lib/libopencv_imgproc.so.3.4

)

target_link_libraris(target
LiBS)
```