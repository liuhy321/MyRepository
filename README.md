# 将代码推送到GitHub仓库

- 打开命令行终端(如Windows的命令提示符或Mac的终端)。
- 使用`cd`命令切换到你的文件所在的目录。
- 运行以下命令初始化本地Git仓库：

  ```bash
  git init
  ```

- 运行以下命令从远程仓库克隆一个完整的仓库到本地：

  ```bash
  git clone [url]
  ```

- 运行以下命令添加一个新的远程仓库引用：

  ```bash
  git remote add [name] [url]
  ```

- 运行以下命令将文件的更改添加到暂存区(staging area)，准备提交：

  ```bash
  git add [file]
  ```

- 运行以下命令将当前目录下的所有更改(包括新文件、修改过的文件)添加到暂存区：

  ```bash
  git add [file]
  ```

- 运行以下命令提交暂存区的更改到本地仓库，并附上提交信息：

  ```bash
  git commit -m "提交信息"
  ```

- 运行以下命令查看工作目录和暂存区的状态，包括哪些文件被修改、哪些文件被暂存等：

  ```bash
  git status
  ```

- 运行以下命令显示提交历史，包括每次提交的哈希值、作者、日期和提交信息：

  ```bash
  git log
  ```

- 运行以下命令显示工作目录中文件的未暂存更改：

  ```bash
  git diff
  ```

- 运行以下命令显示已经暂存的文件与上次提交之间的差异：

  ```bash
  git diff --cached
  ```

- 运行以下命令从远程仓库获取数据，不进行合并：

  ```bash
  git fetch [remote]
  ```

- 运行以下命令从远程仓库拉取数据，并于当前分支合并：

  ```bash
  git pull [remote] [branch]
  ```

- 运行以下命令将本地分支的更改推送到远程仓库：

  ```bash
  git push [remote] [branch]
  ```

- 运行以下命令将你的代码推送到GitHub仓库：

  ```bash
  git push -u origin master
  ```

- 运行以下命令创建一个新分支：

  ```bash
  git branch [branch_name]
  ```

- 运行以下命令切换到指定的分支：

  ```bash
  git checkout [branch_name]
  ```

- 运行以下命令将另一个分支的更改合并到当前分支：

  ```bash
  git merge [branch]
  ```

- 运行以下命令将当前分支的更改应用到另一个分支的基础上，重新定位提交：

  ```bash
  git rebase [branch]
  ```

- 运行以下命令给当前提交打上一个标签，通常用于标记分布版本：

  ```bash
  git tag [tag_name]
  ```

- 运行以下命令将HEAD指针移动到指定的提交，但不会影响工作目录：

  ```bash
  git reset [commit]
  ```

- 运行以下命令创建一个新的提交，撤销指定提交的更改：

  ```bash
  git revert [commit]
  ```

- 运行以下命令将当前工作目录的更改保存起来，以便之后恢复：

  ```bash
  git stash
  ```

- 运行以下命令恢复最近一次保存的stash，并从stash列表中删除它：

  ```bash
  git stash pop
  ```

- 运行以下命令清除工作目录中的未跟踪文件：

  ```bash
  git clean -f
  ```

- 一个文件，用于指定哪些文件或目录不应该被Git跟踪。

  ```bash
  .gitignore
  ```
