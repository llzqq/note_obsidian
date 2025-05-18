#snake

>函数列表
`snake_cell_at`
`set_rect_xy_`
`put_cell_at_`
`are_cells_full_`
`new_food_pos_`
`wrap_around_`

---
#宏
```
 #define SHIFT(x, y) ((x) + ((y) * SNAKE_GAME_WIDTH)) * SNAKE_CELL_MAX_BITS
 ```
`(x) + ((y) * SNAKE_GAME_WIDTH)`计算一维索引
再 `* SNAKE_CELL_MAX_BITS` 得到偏移量
最终实现将二维坐标转化为一一对应的一维数组

---


