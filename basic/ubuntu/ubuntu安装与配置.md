

#### make install详情
>`指定安装位置 sudo make install DESTDIR=/home/lzq/packges/g2o/install
 CMakeLists.txt 或 Makefile 配置文件中的MAKE_INSTALL_PREFIX变量值，默认为/usr/local 。`
```
可执行文件：/usr/local/bin
库文件：/usr/local/lib
头文件：/usr/local/include
共享资源：/usr/local/share
```
#### 安装与卸载   
```bash
# .deb文件安装
sudo apt install hello.deb
sudo dpkg -i hello.deb
sudo dpkg -l | grep “a”
sudo dpkg -r 软件名
```
```bash
# 对应make install
sudo make unistall
sudo rm -rf /usr/local/include/glog/
sudo rm -rf /usr/local/lib/libglog*

# 对应dpkg
sudo dpkg -r package_name 

# 对应apt install
sudo apt-get remove
```

#### 文件查找
```bash
# 更新索引
sudo updatedb

locate glog
```


#### fish
	wget http://fishros.com/install -O fishros && . fishros

#### others
	amd64 = X86_64 笔记本电脑
	arm64 是嵌入式设备