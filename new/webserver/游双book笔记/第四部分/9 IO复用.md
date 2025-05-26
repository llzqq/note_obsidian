I/O复用：一个程序能同时监听多个文件描述符

- **select**
在一段指定时间内，监听用户感兴趣的文件描述符上的可读、可写和异常等事件
然后作出反应
```cpp
#include＜sys/select.h＞
int select(int nfds,fd_set*readfds,fd_set*writefds,fd_set*exceptfds,struct
timeval*timeout);
```
- **poll**
在指定时间内轮询一定数量的文件描述符，以测试其中是否有就绪者
```cpp
#include＜poll.h＞
int poll(struct pollfd*fds,nfds_t nfds,int timeout);
```
- **epoll**
首先，epoll使用一组函数来完成任务，而不是单个函数。
其次，epoll把用户关心的文件描述符上的事件放在内核里的一个事件表中，从而无须像select和poll那样每次调用都要重复传入文件描述符集或事件集。
但epoll需要使用一个额外的文件描述符，来唯一标识内核中的这个事件表：
`#include＜sys/epoll.h＞
`int epoll_create(int size)
操作epoll的内核事件表：
`#include＜sys/epoll.h＞
`int epoll_ctl(int epfd,int op,int fd,struct epoll_event*event)

- **xinetd**
![[图片：9xinetd.png]]
