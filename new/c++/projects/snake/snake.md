`main.cpp`和`input_handing.cpp`是通用的，不需要过多修改

**`util.cpp`**
是服务于`game_logic.cpp`的
主要定义了游戏的资源结构`SnakeContext`，和辅助函数

**`game_logic.cpp`**
有三个函数
一个初始化函数，为`SnakeContext`初始化
一个处理键盘输入，存储入`SnakeContext`中
一个游戏更新函数，主要的逻辑函数，处理每一帧游戏的进展
