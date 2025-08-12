**检查服务状态：**
systemctl --user status onedrive.service

**查看同步日志：** 如果想查看同步过程中的日志，可以使用：
journalctl --user-unit onedrive -f

**结束同步：**
```bash
systemctl disable --now --user onedrive
```