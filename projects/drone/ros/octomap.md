
查询某一点的占据状态
```cpp
void callback_octomap(const octomap_msgs::Octomap::ConstPtr& msg)

{

// 将二进制消息转换为八叉树对象

octomap::AbstractOcTree* octree = octomap_msgs::binaryMsgToMap(*msg);

if (octree == nullptr) {

ROS_ERROR("Failed to deserialize Octomap message");

return;

}

  

// 动态转换为 OcTree

octomap::OcTree* occupancy_octree = dynamic_cast<octomap::OcTree*>(octree);

if (occupancy_octree == nullptr) {

ROS_ERROR("Failed to cast to OcTree");

delete octree; // 释放八叉树对象

return;

}

  

// 查询目标点的占据状态

if(get_targetXY){

// 目标点

octomap::point3d query_point(targetXY.x, targetXY.y, 0.05);

octomap::OcTreeNode* node = occupancy_octree->search(query_point);

if (node != nullptr && occupancy_octree->isNodeOccupied(node)) {

ROS_INFO("Point (%f, %f, %f) is occupied", query_point.x(), query_point.y(), query_point.z());

} else {

ROS_INFO("Point (%f, %f, %f) is not occupied", query_point.x(), query_point.y(), query_point.z());

}

}

  

delete octree; // 释放八叉树对象

}
```
遍历所有点
```cpp
octomap::AbstractOcTree* tree = octomap_msgs::msgToMap(*msg);
    if (!tree)
    {
        ROS_ERROR("Failed to convert message to octomap");
        return;
    }

    // 遍历八叉树
    for (octomap::OcTree::leaf_iterator it = tree->begin_leafs(); it != tree->end_leafs(); ++it)
    {
        octomap::point3d node_position = it.getCoordinate();
        bool is_occupied = tree->isNodeOccupied(*it);
        ROS_INFO("Node at (%f, %f, %f) is %s", node_position.x(), node_position.y(), node_position.z(), is_occupied ? "occupied" : "free");
    }

    delete tree;
```
获取边界
```cpp
octree->getMetricMax(map_border_max[0], map_border_max[1], map_border_max[2]);

octree->getMetricMin(map_border_min[0], map_border_min[1], map_border_min[2]);
```