**`editorRowsToString`**
```cpp
p = buf = (char*)malloc(totlen);
for (j = 0; j < E.numrows; j++) {
	memcpy(p,E.row[j].chars,E.row[j].size);
	p += E.row[j].size;
	*p = '\n';
	p++;
}
*p = '\0';
return buf;
```
用到了“游标指针模式”，
起始指针保持对分配内存的引用，方便最终返回或释放；
游标指针负责在内存区域内移动并执行读写操作。