
#### gitee
qqlzqqq
c2a95933a463ae8d9a321c62db93fda7

#### 连接github空仓库
git init
git add .    （自动暂存当前目录下的所有修改、新增和删除）
git commit -m "Initial commit"
git remote add origin git@github.com:llzqq/note_obsidian.git
git push -u origin master

#### 若github仓库已经有内容
git init
git remote add origin git@github.com:llzqq/self-llm.git
git pull origin master


#### 取消提交某个文件
git restore --staged <文件>   （仍然被 Git 跟踪）
git rm --cached <文件名>       （停止被 Git 跟踪）

#### 分支
git checkout