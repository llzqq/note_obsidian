
**开启调试**
```cmake
# 设置编译器选项以支持调试
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -ggdb -Wall -W -pedantic")

-g：生成调试信息，使 GDB 能够读取变量和函数的详细信息。
-Wall：启用所有警告消息。 
-W：启用额外的警告消息。
-pedantic：启用 ISO C 标准的严格检查，警告不符合标准的代码。
-O0：禁用优化，使调试更加准确。
-ggdb：生成更详细的调试信息，专为 GDB 设计。
```
**常用命令**

| 命令                | 缩写  | 说明                                                    |
| ----------------- | --- | ----------------------------------------------------- |
| run               | r   | 开始执行程序                                                |
| break \<location> | b   | 设置断点，<br>如 `b main`、`b file.cpp:10`、`b Class::Method` |
| next              | n   | 执行下一行，不进入函数                                           |
| step              | s   | 执行下一行，进入函数                                            |
| continue          | c   | 继续运行直到下一个断点                                           |
| print \<expr>     | p   | 打印变量或表达式，<br>如`p variable`、`p *ptr`                   |
| list              | l   | 显示当前位置的源代码                                            |
| backtrace         | bt  | 查看调用栈                                                 |
| ino breakpoints   | i b | 查看所有断点                                                |
| delete \<num>     | d   | 删除断点，如`d 2`                                           |
| watch \<expr>     |     | 监视表达式变化（当值改变时暂停）                                      |
| quit              | q   | 退出                                                    |

**调试基本流程**
1. 设置断点在 `main` 函数：
    (gdb) b main
2. 运行程序：
    (gdb) run
3. 逐行执行（`next`/`step`）并打印变量：
    (gdb) p a
    (gdb) p b
4. 当程序崩溃时，查看调用栈：
    (gdb) bt

调试已经运行的程序
```
sudo gdb -p `pidof ...`
```

**vscode内调试**
