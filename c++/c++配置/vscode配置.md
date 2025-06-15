### tasks.json
`这个模板需要在src这一级目录使用`
之后直接按下`Ctrl + Shift + B`就可生成可执行文件
```json
{
    "version": "2.0.0",
    "tasks": [
        {
			"label": "cmake configure",  //任务的名称，用于在 VSCode 中标识这个任务
            "type": "shell",  //VSCode 会启动一个终端会话来执行指定的命令
            "command": "cmake",  //指定要运行的命令
			"args": [  //指定传递给 `cmake` 命令的参数
                "-B",  //构建生成的文件（如 Makefile 等）
                "${workspaceFolder}/build",  //将放在项目根目录下的 `build` 文件夹中
                "-S",  //表示 CMakeLists.txt 文件所在的目录
                "${workspaceFolder}",
                "-DCMAKE_BUILD_TYPE=Debug"  //构建类型
            ],
            "group": {
                "kind": "build",
				"isDefault": false  //表示这个任务不是默认的构建任务。默认任务是当你按下 `Ctrl + Shift + B` 时 VSCode 会自动运行的任务
            },
            "problemMatcher": ["$gcc"],
            "detail": "Configure the project with CMake"
        },
        {
            "label": "cmake build",
            "type": "shell",
            "command": "cmake",
            "args": [
                "--build",
                "${workspaceFolder}/build",
                "--config",
                "Debug"
            ],
            "dependsOn": ["cmake configure"],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": ["$gcc"],
            "detail": "Build the project with CMake"
        }
    ]
}
```


### launch.json
`需要调整program 可执行文件`
`按下f5调试`

| 变量名                          | 示例值                      | 用途            |
| ---------------------------- | ------------------------ | ------------- |
| `${workspaceFolder}`         | `/home/user/project`     | 项目根目录绝对路径     |
| `${fileDirname}`             | `/home/user/project/src` | 当前打开文件所在目录    |
| `${fileBasenameNoExtension}` | `main`                   | 当前打开文件名（无扩展名） |
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "C++ Debug",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/build/${fileBasenameNoExtension}", // 可执行文件路径
      "args": [], // 命令行参数，如程序需要接受文件名
      "stopAtEntry": false,
	  "cwd": "${workspaceFolder}",  //指定调试器启动时的工作目录，程序依赖外部文件时
      "environment": [],
      "externalConsole": false,
      "MIMode": "gdb",
      "miDebuggerPath": "/usr/bin/gdb", // 调试器路径（Windows 为 MinGW 的 gdb.exe）
      "setupCommands": [
        {
          "description": "为 gdb 启用整齐打印",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ],
      "preLaunchTask": "Build" // 调试前执行的任务,tasks.json中的lable
    }
  ]
}
```

#### 一些插件
**clang-format**
```bash
# 自动化整理格式
# 安装
sudo apt install clang-format  # 系统安装
clang-format   # vscode安装
# 得到配置文件
clang-format -style=google -dump-config > .clang-format
# vscode settings.json配置
"editor.formatOnSave": true,
"clang-format.style": "file",
"clang-format.assumeFilename": "/home/lzq/.clang-format",
"clang-format.executable": "/usr/bin/clang-format",
"clang-format.fallbackStyle": "Google",
"editor.defaultFormatter": "xaver.clang-format"
```
