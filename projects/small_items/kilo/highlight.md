**`C_HL_extensions`的定义**
#指针 
```cpp
const char *C_HL_extensions[] = {".c",".h",".cpp",".hpp",".cc",NULL};

struct editorSyntax {
	const char **filematch;
	...
};

struct editorSyntax HL = {
	C_HL_extensions,
	...
}
```
首先`const char *`定义的是`const char`类型的指针，
`C_HL_extensions[]`表示这是一个存储指针的数组
而当只写数组名`C_HL_extensions`时，代表的是指向该数组第一个位置的指针

**`HLDB_ENTRIES`**
#数组 
```cpp
editorSyntax HLDB[] = {
{
	C_HL_extensions,
	C_HL_keywords,
	{'/', '/'},{'/', '*'},{'*', '/'},
	HL_HIGHLIGHT_STRINGS | HL_HIGHLIGHT_NUMBERS
}
};

const unsigned int HLDB_ENTRIES = sizeof(HLDB) / sizeof(HLDB[0]);
```
最基本的数组，是没有任何操作的函数的，比如获取大小，只能手动计算得到


**`strstr`**
#字符串 
```cpp
char *strstr(char *__haystack, const char *__needle)

char *p;
p = strstr(filename,s->filematch[i])) 
```
strstr在__haystack中寻找__needle，并且返回匹配字符以后的内容

**`const char*`**
#字符串
`const char* a = "me.cpp";`
字符串字面量通常存储在只读内存区域，尝试修改它们会导致未定义行为。
这种C风格字符串，修改内容时内存大小需要手动分配


**editorUpdateSyntax太繁琐了，没仔细看**
