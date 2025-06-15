#### 基础运行
rosbag record -a -x "(.*)/Scene(.*)"

rosbag record -o whole.bag /bbb/target/get_targetZ_target  /bbb/target/get_targetXY_latest  /bbb/target/get_targetXY_unbroken  /glim_ros/odom airsim_node/drone_1/front_left/Scene
#### bag编辑
```
rosbag record -O name.bag topic1 topic2

rosbag filter input.bag output.bag "topic == '/odom' or topic == '/imu'"
 #摘取指定话题
```
