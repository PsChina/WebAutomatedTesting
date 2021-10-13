# Selenium 开发环境搭建

1. 打开[https://wwww.python.org](https://wwww.python.org)
1. 选择合适版本下载到电脑（windows 需要配置环境变量，安装时建议自定义安装，选择一个熟悉的路径）

## python 环境变量的配置

### Windows

1. 在安装路径下找到 python.exe 复制路径
1. 右键单击此电脑->属性->高级系统设置->环境变量
1. 在环境变量里面找到系统变量里面的path打开
1. 在path里面新建一个路径粘贴第一步复制好的路径
1. 打开命令行输入 python 验证是否安装配置成功

### Mac

1. which python3 复制路径 （which python）
1. cd ~/
1. vi .bash_profile
1. o
1. 粘贴路径到 .bash_profile
1. esc :wq


## pip 环境变量的配置

### Windows

1. 在 python 安装路径下有一个 Script 文件夹打开它可以看到里面有一个 pip.exe。
1. 复制这个路径。
1. 和配置 python.exe 一样吧 pip.exe 也设置到 系统变量 里面的 path 里面。
1. 打开命令行输入 pip list 验证是否配置成功


### Mac

1. which pip3 复制路径 （which pip）
1. cd ~/
1. vi .bash_profile
1. o
1. 粘贴路径到 .bash_profile
1. esc :wq



### 安装 Selenium 模块


1. 打开命令行 pip install selenium 回车 (如果是pip3 请使用 pip3 install selenium)

如果 mac 安装的时候权限不够 请使用 pip install --user selenium 或者  pip3 install --user selenium

## 下载安装浏览器驱动

1. 查看浏览器版
1. 打开 Selenium 官网: [https://www.selenium.dev](https://www.selenium.dev)
1. Getting Started -> Installing browser drivers
1. 选择对应浏览器内核的驱动下载对应浏览器版本的驱动

mac 安装需要允许安装非 AppStore 来源的应用

