#### 基础运行

```
rosrun rqt_tf_tree rqt_tf_tree

rosrun tf tf_monitor camera_init aft_mapped
rosrun tf tf_echo camera_init aft_mapped

rosrun map_server map_saver  map:=/projected_map -f ~/map
```
#### launch文件中静态tf

```
<node pkg="tf" type="static_transform_publisher" name="baselink_lidar" args="0 0 0.08 0 0 0 base_link iris_0/laser_3d 100" />

<node pkg="tf" type="static_transform_publisher" name="map_camera" args="0 0 0 0 0 0 camera_init map 100" />
```
#### tf转换
```cpp
#include "ros/ros.h"
#include "tf2_ros/transform_listener.h"
#include "tf2_ros/buffer.h"
#include "geometry_msgs/PointStamped.h"
#include "tf2_geometry_msgs/tf2_geometry_msgs.h" // 包含TF坐标转换方法

// 创建TF缓冲区和监听器
tf2_ros::Buffer buffer;
tf2_ros::TransformListener listener(buffer);

// 直接转换
try
{
	// 转换点到目标坐标系
	geometry_msgs::PointStamped point_target;
	point_target = buffer.transform(point_source, "target_frame"); // 目标坐标系名称

}
catch (const std::exception &e)
{
	ROS_ERROR("坐标转换失败: %s", e.what());
}

// 拿到转换关系，后续需要进一步处理
const auto trans_imu_base = tf_buffer.lookupTransform(imu_frame_id, base_frame_id, stamp);

```

#### 关系理解
**世界坐标(map)**
固定系，真实的世界坐标系，即机器人的真实位置，实际中需要校正给出

**里程计坐标系(odom)**
固定系（指坐标系原点固定在0，0，0），机器人以为的世界坐标系，以为自己在的位置

**基坐标系(base_link)**
base_link坐标系是机器人本体坐标系，它可以安装在基座中的任意方位。
（随机器人移动）

**雷达坐标系(base_laser)**
base_laser坐标系是激光雷达的坐标系，与激光雷达的安装点有关。


***base_link + 里程计 ---->  odom + 校正 ------>  map***

----------------------------------------------------------------------
camera_init 是固定坐标系，以初始时刻为原点，相当于map
aft_mapped 相当于base_link
local_position的数据通过aaa_lidar_tf发布，计算 aft_mapped 相对camera_init 运动的坐标

----------------------------------------------------------------------
无人机的gazebo模型是基于base_link的，但tf_tree没有到map的tf信息
感觉是mavros或者px4内部写的转换