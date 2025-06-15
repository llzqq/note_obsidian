- **pipe**函数可用于创建一个管道，以实现进程间通信
```cpp
#include＜unistd.h＞
// fd[0]只能用于从管道读出数据，fd[1]则只能用于往管道写入数据
// 往fd[1]写入的数据可以从fd[0]读出
// 阻塞的。此时如果我们用read系统调用来读取一个空的管道，则read将被阻塞，直到管道内有数据可读
int pipe(int fd[2]);
```

- **dup**把标准输出重定向到 连接socket 的文件描述符
- 发送过程
1. 数据首先进入 TCP 发送缓冲区
2. TCP 协议栈会根据其算法（考虑滑动窗口、Nagle 算法等）决定何时将数据发送出去
```cpp
#include＜unistd.h＞
// dup函数创建一个新的文件描述符，该新文件描述符和原有文件描述符file_descriptor指向相同的文件、管道或者网络连接。并且dup返回的文件描述符总是取系统当前可用的最小整数值。
int dup(int file_descriptor);
```

- readv函数将数据从文件描述符读到分散的内存块中，即分散读
- **writev**函数则将多块分散的内存数据一并写入文件描述符中，即集中写
```cpp
#include＜sys/uio.h＞
ssize_t readv(int fd,const struct iovec*vector,int count)；
ssize_t writev(int fd,const struct iovec*vector,int count);
```

- **sendfile**函数在两个文件描述符之间直接传递数据（完全在内核中操作）
```cpp
#include＜sys/sendfile.h＞
// in_fd 是文件
// out_fd 是 socket
ssize_t sendfile(int out_fd,int in_fd,off_t*offset,size_t count);
```

- **mmap**函数用于申请一段内存空间。我们可以将这段内存作为进程间通信的共享内存，也可以将文件直接映射到其中。munmap函数则释放由mmap创建的这段内存空间
```cpp
#include＜sys/mman.h＞
void*mmap(void*start,size_t length,int prot,int flags,int fd,off_t offset);
int munmap(void*start,size_t length);
```

- **splice**函数用于在两个文件描述符之间移动数据，也是零拷贝操作
```cpp
#include＜fcntl.h＞
ssize_t splice(int fd_in,loff_t*off_in,int fd_out,loff_t*off_out,size_t len,unsigned int flags);
```

- **tee**函数在两个管道文件描述符之间复制数据，也是零拷贝操作。
```cpp
#include＜fcntl.h＞
ssize_t tee(int fd_in,int fd_out,size_t len,unsigned int flags);
```
