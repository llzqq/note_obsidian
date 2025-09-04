- 基本查看图像--ros
https://github.com/orbbec/ros2_astra_camera

- 写了一个基本的距离检测

各软件包说明
- openni：比较老的开源框架，只能查看深度图，彩色图有问题，不支持ros。
- uvc：底层的图像框架，可以被整合使用，只能查看彩色图。
- orbbecviewer：奥比中光自己的图像查看器，但是显示有问题。
- orbbecsdk：依然深度图有问题。
- ros2_astra_camera：可以正常使用，怀疑sdk更多适配gemini等新相机，astra专门是这个系列的。