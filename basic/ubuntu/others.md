#### 端口
lsusb

#### 文件传输
- 传输文件给别人
scp  ./file.txt  usrname@ip:  ~/target/folder

- 把别人文件传给自己
scp  usrname@ip: ~/flie.txt  ~/self/folder

#### 防火墙
- 查看ufw防火墙状态
 sudo ufw status verbose

- 添加规则
sudo ufw allow 1234/tcp

#### 清理垃圾
- 日志
  sudo rm -rf /var/log/*.gz
- 缓存
  rm -rf ~/.cache/*

#### 输入法
- 希腊字符等
gucharmap

#### 图像
- 改变大小
convert 3_0p2.png -resize 500 3_0p2.png

#### 自动登陆
/etc/gdm3/custom.conf