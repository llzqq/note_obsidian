```cpp
/*
	客户端 <---> 服务器 <---> mysql数据库
		   ^^^
		thread_pool
*/
```
- 预先创建 n个线程，利用信号量`m_queuestat.wait()`,让线程都挂起,直到有连接时唤醒一个
- 初始化线程
```cpp
pool = new threadpool<http_conn>(connPool);
// 构造函数中,核心为这句
// 线程创建好之后,立即运行worker函数
if (pthread_create(m_threads + i, NULL, worker, this) != 0) {
...}
// worker函数
// 线程中的对象都是同一个
threadpool *pool = (threadpool *)arg;
pool->run();
// run函数
// 一进入就等待,被唤醒之后才拥有锁.最后将资源交给 http_conn 的 mysql
m_queuestat.wait();
m_queuelocker.lock();
...
connectionRAII mysqlcon(&request->mysql, m_connPool);
```