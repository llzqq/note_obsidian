
### docker

```cpp
# 生成最终的可以直接运行程序的镜像文件
docker build -t program_dev .

# 运行该镜像文件，会直接执行程序
docker run -it --net host --name test_dev --rm 
docker run -it --net host --name new --rm  new

# 如果镜像文件运行没有问题就可以导出为压缩包上传了
docker image save test_dev:latest > test.tar


# 删除镜像
docker rmi 

# 删除容器
docker rm

# 全部清理
docker system prune -a
```

### Dockerfile

```cpp
FROM osrf/ros:noetic-desktop-full-focal
ADD src /new/src/
ADD gtsam /new/thirdparty/gtsam
ADD gtsam_points /new/thirdparty/gtsam_points
ADD Livox-SDK /new/thirdparty/Livox-SDK
ADD eigen-3.3.7 /new/thirdparty/eigen
ADD cmake /new/thirdparty/cmake
ADD setup.bash /

RUN chmod +x /setup.bash

USER root

RUN  truncate -s 0 /etc/apt/sources.list                
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse" |  tee /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse" |  tee -a /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse" |  tee -a /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse" |  tee -a /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse" |  tee -a /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse" |  tee -a /etc/apt/sources.list


RUN apt-get update && apt-get install -y python3-catkin-tools ros-noetic-geographic-msgs \
 ros-noetic-tf2-sensor-msgs ros-noetic-tf2-geometry-msgs ros-noetic-image-transport \
 net-tools ros-noetic-nav-msgs ros-noetic-tf2-eigen ros-noetic-tf2 \
 ros-noetic-message-filters ros-noetic-visualization-msgs
 


RUN apt-get install -y ros-noetic-octomap-mapping ros-noetic-octomap-msgs \
			ros-noetic-octomap-ros  ros-noetic-octomap-server


RUN apt-get install -y libomp-dev libboost-all-dev libmetis-dev \
                 libfmt-dev libspdlog-dev libparmetis-dev\
                 libglm-dev libglfw3-dev libpng-dev libjpeg-dev libssl-dev libtbb-dev ros-noetic-mavros-msgs

RUN cd /new/thirdparty/cmake && ./bootstrap && make -j8 && make install
RUN cd /new/thirdparty/eigen && mkdir build && cd build && cmake .. && make -j6 && make install

RUN cd /new/thirdparty/Livox-SDK && cd build && cmake .. && make -j8&& make install

RUN cd /new/thirdparty/gtsam && mkdir build && cd build && 	cmake .. -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
         -DGTSAM_BUILD_TESTS=OFF \
         -DGTSAM_WITH_TBB=OFF \
         -DGTSAM_USE_SYSTEM_EIGEN=ON \
         -DGTSAM_BUILD_WITH_MARCH_NATIVE=OFF	&& make -j8 && make install

RUN cd /new/thirdparty/gtsam_points &&  mkdir build && cd build && cmake .. && make -j6 && make install

ENV ROS_DISTRO noetic
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

WORKDIR /new/
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && catkin_make --only-pkg-with-deps airsim_ros && . devel/setup.sh && catkin_make --only-pkg-with-deps control && catkin_make --only-pkg-with-deps glim && catkin_make --only-pkg-with-deps glim_ros && catkin_make --only-pkg-with-deps guide

ENTRYPOINT [ "/setup.bash" ]

```