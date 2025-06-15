```cpp
/* ======================= Editor rows implementation ======================= */
/* Update the rendered version and the syntax highlight of a row. */
void editorUpdateRow(erow *row);

/* Insert a row at the specified position, shifting the other rows on the bottom
* if required. */
void editorInsertRow(int at, const char *s, size_t len);

/* Free row's heap allocated stuff. */
void editorFreeRow(erow *row);

/* Remove the row at the specified position, shifting the remainign on the
* top. */
void editorDelRow(int at);

/* Insert a character at the specified position in a row, moving the remaining
* chars on the right if needed. */
void editorRowInsertChar(erow *row, int at, int c);

/* Append the string 's' at the end of a row */
void editorRowAppendString(erow *row, char *s, size_t len);
  
/* Delete the character at offset 'at' from the specified row. */
void editorRowDelChar(erow *row, int at);

/* Insert the specified char at the current prompt position. */
void editorInsertChar(int c);

/* Inserting a newline is slightly complex as we have to handle inserting a
* newline in the middle of a line, splitting the line as needed. */
void editorInsertNewline(void);

/* Delete the char at the current prompt position. */
void editorDelChar(void);
```

太多函数了，而且都是行操作的具体实现，好像没有语法点
所以没看
