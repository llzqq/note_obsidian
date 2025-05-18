**得到当前时刻附近点云-->xy平面道路-->道路下点-->障碍物识别**


```
glim_ros/points -->  cloud_fuse -->  bbb/points/fused -->	octomap

octomap --> /map --> get_target-->  /bbb/target/roadCenter_unbroken_map 
									/bbb/target/roadCenter_latest_map
									| 
		        --> /octomap_binary -->target_z --> /bbb/target/roughTarget
									

```

glim_ros/points -->  **cloud_fuse** -->  bbb/points/fused

bbb/points/fused -->	**octomap** --> /map  &&   /octomap_binary

/map -->   **get_target**  -->  /bbb/target/roadCenter_unbroken_map && /bbb/target/roadCenter_latest_map
+
/octomap_binary -->  **target_z**  --> /bbb/target/roughTarget

#### get_targetXY.cpp

>input:  image_map
>**image_preprocess(Mat &image_map)**
>
**FirstSegment_backY**:  拟合的第一段墙的尾部y的值
**currntBackYPos**:  当前图像显示的，第一段墙尾部y的值
**topSideWall_offset** ：图像向下偏移
>
> **road_detect(const Mat &image)**
**roadCenterXY_latest_map**
**roadCenterXY_unbroken_map**


#### get_targetZ.cpp

**callback_roadCenterXY_unbroken(const geometry_msgs::PointConstPtr &msg)**
根据是否接收到新的`currentTargetXY_unbroken`，并且受`ifBottomZ_NotReady`调控
最终给 `ifDeleteOctree` 赋值

**callback_octomap(const octomap_msgs::Octomap::ConstPtr& msg)**
`/octomap_binary`的回调函数，根据 `ifDeleteOctree`
调用`getBottomof_roadCenter()`，得到`getBottomof_roadCenter()`

**callback_roadCenterXY_latest(const geometry_msgs::PointConstPtr &msg)**
发送最终的目标点



#### 当前点云合成
直接对相邻三个时间戳的点云相加，不过在lidar系下会漂移。
所以先转到map系下合成，再转回lidar系发布。
另外一开始对点云进行裁减，只需要道路的点云

**cloud_fuse.cpp**
/glim_ros/points -->/bbb/points/fused
拿到原始点云，处理融合之后发布
根据道路中心点的变化，给octomap道路中心点两边各62像素点的points

**octomap**
/bbb/points/fused --> /map
octomap处理得到二维和三维栅格地图
#### 道路识别
得到道路的点云之后，使用octomap，得到2维OccupancyGrid地图，以及三维的占位地图，方便后续使用。

**get_map.cpp**
/map --> /bbb/map_image
简单的得到二维栅格地图数据，OccupancyGrid

**image.cpp**
得到道路和障碍物的位置

***Mat  Sense::image_preprocess(Mat image_map)***
使用opencv扩张再缩减，进行预处理，使道路两侧更明显
![[after.png]]

***mypair  Sense::road_detect(const Mat& image )***
得到道路中心点
![[152result_image.jpg]]
`用x长度是否足够长，以及两侧间的距离来判断，是否为路`
`上下两侧，如果某个点为black且向右30均为black，那么这一条肯定是wall`
`中间部分，向右40，为障碍物`
初始化一条topSide_Wall代表整条路，part_topSide_Wall代表每一段，初定170个像素点，中间的door初定40个像素点。
用前一段拟合出下一段part_topSide_Wall，然后根据图像after修正此part_topSide_Wall。
part_topSide_Wall的弯曲量是从顶点开始，关于长度的二次函数

***`void findWallPositions(const Mat& image, vector<WallSegment>& wallSegments)`***
根据前一段墙的函数初始化下一段墙，然后修正
只有在图像宽度比current_length多180个像素点时，才会进行完整的segment判断
否则会在lastSegment_length>60时进行残余墙的判断

***`void correctSegment(WallSegment& segment, const Mat& image, int iterations )`***
在当前直线的附近找到黑点，根据黑点集拟合出新的直线，当作当前墙段




