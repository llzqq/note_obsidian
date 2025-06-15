### 以indoor1.launch为例
#### empty_world.launch+indoor1.world
创建基本的世界，如屋子，桌子这些

#### single_vehicle_spawn_xtd.launch
1. 打开px4和gazebo_ros两个node，加载参数\<param command="\$(arg cmd)" name="model_description"/>，创建无人机模型和飞控
<br>

2. px4创建仿真环境的飞控
<br>
3. gazebo\_ros
\<node name="\$(arg vehicle)_\$(arg ID)_spawn" output="screen" 
pkg="gazebo_ros" 
type="spawn_model" 
args="  -sdf 
		-param model_description 	
		-model \$(arg vehicle)_\$(arg ID_in_group) 
		-x $(arg x) -y $(arg y) -z $(arg z) -R $(arg R) -P $(arg P) -Y $(arg Y)"/>
> spawn_model读取一个模型的描述，并将其实例化到Gazebo仿真中
-sdf指定读取sdf格式的文件
-param model_description让spawn_model读取 /model_description下的模型描述			
-model \$(arg vehicle)_$(arg ID_in_group) 指定名字

#### gazebo话题
```
gz -l topic
gz -i topic /gazebo/default/iris_0/vision_odom
```

#### iris_3d_lidar.sdf
\<link name='base_link'>		为部件指定坐标系和在此坐标系的位置等物理属性
\<joint name='/imu_joint' type='revolute'>		指定/imu_link和base_link的相对位置等
  	\<child>/imu_link</child>
    \<parent>base_link</parent>



#### .world创建
1.	在gazebo中创建世界模型
2.	save world
3.	在launch文件中    
\<arg name="world_name" value="~/worlds/house.world"/> 

.world里面的uri
>路径是相对工作环境的，工作环境是gazebo_ros
所以材料要放进gazebo_ros里面
可以在package.xml里设定

model_path
/home/lzq/.gazebo/gui.ini
model path = /.gazebo/models