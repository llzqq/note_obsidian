#### velodyne_laser:
libgazebo_ros_velodyne_laser.so

#### livox :
liblivox_laser_simulation.so
通过livox_laser_simulation发布仿真数据，但是现有的发布格式和算法不兼容
具体为header没有time 或insten..

livox_ros_driver2/CustomMsg
sensor_msgs/PointCloud2

### 运行
#### 仿真环境
roslaunch turtlebot3_gazebo turtlebot3_house.launch

#### 配置tf tree
roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
rviz add laserscan 需要tf才能发布scan
/gazebo通过urdf文件发布/joint_states(需要自己发布)，robot_state_publisher根据其发布tf

#### SLAM
rosrun gmapping slam_gmapping
需要在rviz add map
gmapping读取scan和tf发布map，比较特殊的是gmapping发布的是位置范围
使用的是gazebo发布的odom

#### 导航
roslaunch turtlebot3_navigation move_base.launch
move_base读取map odom tf
rviz add path