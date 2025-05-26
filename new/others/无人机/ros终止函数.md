
#### 使用signal
```cpp
#include <signal.h>

void mySigintHandler(int sig) {

ROS_INFO("Received SIGINT, shutting down node.");

if (csv_file.is_open()) {

	csv_file.close();
	
	ROS_INFO("CSV file closed on shutdown.");
	
	// 调用 ros::shutdown() 关闭节点
	
	ros::shutdown();

}
int main()
{
	signal(SIGINT, mySigintHandler);
}

}
```

#### 使用析构函数
析构函数的作用就是在类结束时，关闭一些东西
```cpp
~Get_road() {

if (csv_file.is_open()) {

csv_file.close();

ROS_INFO("CSV file closed on shutdown.");

}

}
```