# 将代码推送到GitHub仓库

- 打开命令行终端(如Windows的命令提示符或Mac的终端)。
- 使用`cd`命令切换到你的文件所在的目录。
- 运行以下命令初始化本地Git仓库：
  ```
  git init
  ```

- 运行以下命令关联你的本地仓库与GitHub远程仓库：
  ```
  git remote add origin <仓库的URL地址>
  ```

- 运行以下命令将你的文件添加到本地仓库：
  ```
  git add .
  ```

- 运行以下命令提交你的更改：
  ```
  git commit -m "添加代码文件"
  ```

- 最后，运行以下命令将你的代码推送到GitHub仓库：
  ```
  git push -u origin master
  ```