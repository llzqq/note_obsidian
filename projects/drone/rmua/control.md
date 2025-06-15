#### pwm控制
***位置环-->速度环-->角度环-->角速度环-->pwm***

**pid调参**
z方向运动很好调，能做到快速的位置控制
xy方向只需要速度控制就行


airsim_node/drone_1/lidar  &&  airsim_node/drone_1/imu/imu -->  **communication**     -->  

/bbb/points   && /bbb/imu  -->  **glim_ros**  -->  /glim_ros/odom  && /glim_ros/points


/bbb/target/waypoints  -->  **control**  -->  /airsim_node/drone_1/rotor_pwm_cmd

#### 如何控制
接收到/bbb/target/waypoints
vx维持在10m/s左右
z是位置控制
主要是yaw和y控制，目前是取无人机前方5m左右的点作为目标点，取yaw=arctan(dy/dx)


#### Note
我定义的map系和imu系，lidar系初始朝向相同
但是airsim里的imu系和map系初始朝向不同，我取的是imu系