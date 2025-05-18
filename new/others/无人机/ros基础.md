

#### 常用运行指令
```
rosrun map_server map_saver  map:=/projected_map -f ~/map
```
```
roswtf  #检查当前ros package有没有问题

echo $ROS_PACKAGE_PATH  #输出ros环境
echo $PYTHONPATH  #输出python环境

readelf -d yourlibrary.so  #输出.so关联信息
ldd /path/to/your/library.so
```
```
echo $ROS_LIBRARY_PATH

rosrun rviz rviz 2> >(grep -v TF_REPEATED_DATA)  #使不输出TF_REPEATED_DATA


rostopic info 

rosmsg show
```

#### 控制频率

**使用`ros::Rate`**
```cpp
    // 设置发布频率为10Hz
    ros::Rate rate(10); // 10Hz[^2^][^7^]

    while(ros::ok())
    {
        // 获取当前点和路径点
        compute_desiredOdom(targetZ.roughTargetWaypoints, targetXY.current_pose_map);

        // 发布目标导航信息
        guideOdom_pub.publish(guideOdom);

        // 等待直到下一个周期
        rate.sleep();
    }
```

**使用定时器**

```cpp
void timerCallback(const ros::TimerEvent&)
{
    // 获取当前点和路径点
    compute_desiredOdom(targetZ.roughTargetWaypoints, targetXY.current_pose_map);

    // 发布目标导航信息
    guideOdom_pub.publish(guideOdom);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "guide");
    ros::NodeHandle nh_guide;

    // 创建Publisher
    ros::Publisher guideOdom_pub = nh_guide.advertise<nav_msgs::Odometry>("/bbb/target/guide", 10);

    // 初始化目标点获取模块
    Get_targetXY targetXY;
    Get_targetZ targetZ;

    // 创建定时器，以10Hz的频率调用timerCallback函数
    ros::Timer timer = nh_guide.createTimer(ros::Duration(0.1), timerCallback); // 0.1秒即10Hz[^5^]

    // 进入ROS事件循环
    ros::spin();

    return 0;
}
```
#### kill
	rosnode kill -a
	pkill -f RMUA-Linux-Shipping
	
	killall -9 gzclient
	killall -9 gzserver

#### grep
	grep "neirong" . -r -n


#### 创建新ros package
```
cd xxx_ws/src
catkin_init_workspace
catkin_create_pkg name rospy std_msgs sensor_msgs geometry_msgs mavros_msgs
```


#### package关系

program <----> mavros <----> px4(drone)

COM_RCL_EXCEPT
4