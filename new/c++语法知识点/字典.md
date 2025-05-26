#字典

```cpp

#include <map>

std::map<int, std::string> dict; // 创建一个字典，键为 int 类型，值为 string 类型

// 插入键-值对
dict[1] = "one";
dict[2] = "two";
dict[3] = "three";

// 访问字典中的值
for (const auto& kv : dict) {
	std::cout << kv.first << " => " << kv.second << std::endl;
}

// 通过键查找值
if (dict.find(2) != dict.end()) {
	std::cout << "Found: " << dict[2] << std::endl;
} else {
	std::cout << "Not found" << std::endl;
}

// 删除键-值对
dict.erase(2);
```