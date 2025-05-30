三级设计，级级调用
**log** -- **block_queue** -- **locker**
#### log
- **单例设计**，`Log::get_instance()->init("ServerLog", 2000, 800000, 0)`创建唯一的对象，方便其他组件访问该类的资源。函数访问是唯一的，对比变量
```cpp
class Log {
public:
static Log *get_instance() // 返回类型为Log指针，类内的静态函数
{
	/*创建作用域为局部，但是生命贯穿程序的静态变量
	同时相当于创建了实例，可以调用各种类的方法
	通过调用get_instance() 就可以访问该实例*/
	static Log instance;
	return &instance;
}
}
```
- 核心函数`Log::get_instance()->write_log`被封装为宏`LOG_INFO`
```cpp
#define LOG_ERROR(format, ...) \
Log::get_instance()->write_log(3, format, ##__VA_ARGS__)
```
#### block_queue
- 实现了一个阻塞队列`m_log_queue`，拿走消息`m_log_queue->pop(single_log)`，放入消息`m_log_queue->push(log_str)`
- 为拿走消息（紧接着写入文件）操作单独开一个线程
- 使用 cond 让 pop 进入 wait

#### locker
- cond 条件变量，为mutex锁设置cond。使线程进入等待，以及唤醒操作
- locker mutex互斥锁，线程中使用`m_mutex.lock()`若未拿到锁会阻塞，拿到锁则独享该锁

