```cpp
/*
	客户端 <---> 服务器 <---> mysql数据库
					   ^^^
					connection_pool
*/
```
- 预先初始化好n 个服务器与mysql 的连接，称为池
```cpp
connectionRAII::connectionRAII(MYSQL **SQL, connection_pool *connPool) {
	*SQL = connPool->GetConnection();
	conRAII = *SQL; // conRAII是需要使用的对象，通过GetConnection得到资源
	poolRAII = connPool; // connPool是已经初始化好的连接池
}
```
- 需要使用时，再给对象已经准备好的资源，称为RAII